# Imports your models/choices structures
from .models import ExamType, SubjectType
from .models import ExamType, SubjectType  # Uses your real database models
from django.shortcuts import render
import json
import requests
from django.shortcuts import render, redirect
from .form import EnquiryForm, ApplyForm
from .models import Stories, Gallery, ExamType, SubjectType
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from datetime import datetime


# Create your views here.


# Enquiry form
def home(request):

    if request.method == "POST":

        form = EnquiryForm(request.POST)

        if form.is_valid():
           # student_name = form.cleaned_data['first_name']
           # last_name = form.cleaned_data['last_name']
            # father_email = form.cleaned_data['email']

            # subject = f'New application sent'
           # message = f"""
            # You have a new application!

            # Name: {student_name}
            # LastName: {last_name}
            # Email: {father_email}
           # """
           # send_mail(
            #  subject,
            #  message,
            #  settings.DEFAULT_FROM_EMAIL,
            #  ['benworldaskills098@gmail.com'],
            #  fail_silently=False
           # )
            form.save()
            messages.success(
                request,  'Enquiry submitted Successfully, We will get back to you via email/phone')

            form = EnquiryForm()

    else:
        form = EnquiryForm()

    return render(request, "index.html", {
        "form": form
    })


def admission(request):
    return render(request, "admission.html")


# application form
def applying(request):
    message = messages.success(
        request,  'Application submitted Successfully, We have receive your application to enroll your kid')
    if request.method == 'POST':
        forms = ApplyForm(request.POST)
        if forms.is_valid():
            # student_name = forms.cleaned_data['student_name']
            # last_name = forms.cleaned_data['student_lastname']
            # father_email = forms.cleaned_data['father_email']

            # subject = f'New application sent'
            # message = f"""
            # You have a new application!

            # Name: {student_name}
            # LastName: {last_name}
            # Email: {father_email}
            # """

         #   send_mail(
            #     subject,
            #  message,
            #   settings.DEFAULT_FROM_MAIL,
            #  ['benworldaskills098@gmail.com'],
            #  fail_silently=False
          #  )
            forms.save()
            # messages.success(
           #     request,  'Application submitted Successfully, We have receive your application to enroll your kid', fail_silently=False)
            forms = ApplyForm()

            # testing out this.....
        return redirect('/', message)

    else:
        forms = ApplyForm()

    return render(request, 'applying.html', {"forms": forms})


def about_us(request):
    return render(request, 'aboutus.html')


def stories(request):
    story = Stories.objects.all()
    return render(request, 'stories.html', {'stories': story})


def gallery(request):
    gallery = Gallery.objects.all()

    return render(request, 'gallery.html', {'gallery': gallery})


def coming(request):
    return render(request, 'coming.html')


#def practice_question(request):
    current_year = datetime.now().year

    exam = request.GET.get('exam')
    subject = request.GET.get('subject')
    year = request.GET.get('year')

    question_data = []
    error_message = None

    if exam and subject and year:
        if exam in ExamType.values and SubjectType.values:

            url = "https://dev.aloc.com.ng/api/v1/questions"
            headers = {
                'X-API-Key': "aloc_OLe2vTzrwmQk0NrJ7EkfYYakOyfJHuth7fVhOzDK"
            }

            params = {
                'examType': exam,
                'subject': subject,
                'year': year,
                'limit': 10
            }

            try:
                response = requests.get(url, headers=headers, params=params)
                if response.status_code == 200:
                    question_data = response.json().get('data', [])
                else:
                    error_message = 'Could not pull question from external service'
            except requests.exceptions.RequestException:
                error_message = "Network connection problem connecting to the ALOC Station servers."
        else:
            error_message = 'Invalide selection parameter criteria'

    context = {
        'exams': [{'slug': value, 'name': label} for value, label in ExamType.choices],
        'subjects': [{'slug': value, 'name': lable}for value, lable in SubjectType.choices],
        'years': [str(y) for y in range(datetime.now().year, 1999, -1)],
        'question_data': question_data,
        'error_message': error_message
    }

    return render(request, 'pstque.html', context)


# def practice_question(request):
    # 1. Capture what the student selected from the URL parameters
    selected_exam_slug = request.GET.get('exam')
    selected_subject_slug = request.GET.get('subject')
    selected_year = request.GET.get('year')

    # 2. Extract values cleanly if they are TextChoices or Model structures
    # This handles both cases without crashing on '.objects'
    try:
        exams_data = [{'slug': val, 'name': lbl}
                      for val, lbl in ExamType.choices]
    except AttributeError:
        # Fallback if it is an iterable database object setup
        exams_data = [{'slug': e.slug, 'name': e.name}
                      for e in ExamType.objects.all()]

    try:
        subjects_data = [{'slug': val, 'name': lbl}
                         for val, lbl in SubjectType.choices]
    except AttributeError:
        # Fallback if it is an iterable database object setup
        subjects_data = [{'slug': s.slug, 'name': s.name}
                         for s in SubjectType.objects.all()]

    # Apply the sticky selection flags safely in Python
    for exam in exams_data:
        exam['is_selected'] = (exam['slug'] == selected_exam_slug)

    for subject in subjects_data:
        subject['is_selected'] = (subject['slug'] == selected_subject_slug)

    # 3. Generate the dynamic years loop list cleanly
    current_year = datetime.now().year
    years_list = [
        {'value': str(y), 'is_selected': (str(y) == selected_year)}
        for y in range(current_year, 1999, -1)
    ]

    questions_data = []
    error_message = None

    # 4. Request past questions from ALOC Station if form is submitted
    if selected_exam_slug and selected_subject_slug and selected_year:
        allowed_exams = [e['slug'] for e in exams_data]
        allowed_subjects = [s['slug'] for s in subjects_data]

        if selected_exam_slug in allowed_exams and selected_subject_slug in allowed_subjects:
            # Change this section inside your views.py if using your current 'aloc_' key
            url = "https://aloc.com.ng"

            headers = {
                "Accept": "application/json",
                # Your legacy token layout
                "X-ALOC-KEY": "aloc_OLe2vTzrwmQk0NrJ7EkfYYakOyfJHuth7fVhOzDK"
            }

            params = {
                "type": selected_exam_slug,     # Legacy requires 'type', not 'examType'
                "subject": selected_subject_slug,
                "year": selected_year
            }

            try:
                response = requests.get(url, headers=headers, params=params)
                if response.status_code == 200:
                    questions_data = response.json().get('data', [])
                else:
                    error_message = f"ALOC API Error (Status: {response.status_code}). Check your key configuration."
            except requests.exceptions.RequestException:
                error_message = "Failed connecting to external ALOC Station servers."
        else:
            error_message = "Invalid selection parameter criteria."

    # 5. Return context data safely down to the HTML template layer
    context = {
        'exams': exams_data,
        'subjects': subjects_data,
        'years': years_list,
        'questions': questions_data,
        'error': error_message
    }

    return render(request, 'pstque.html', context)


ALOC_URL = "https://dev.aloc.com.ng/api/v1/questions"

HTTP_MESSAGES = {
    401: 'The ALOC API key is missing or invalid.',
    403: 'Your ALOC plan does not allow this request.',
    429: 'Too many requests. Wait a minute and try again.',
}


def _normalise(raw):
    """Shape ALOC v1 questions into what the template/JS expects."""
    questions = []
    for item in raw:
        options = {k.lower(): v for k, v in (
            item.get('options') or {}).items() if v}
        questions.append({
            'id': item.get('id'),
            'question': item.get('text') or '',
            'options': dict(sorted(options.items())),
            'answer': (item.get('correctAnswer') or '').lower(),
            'explanation': item.get('explanation') or '',
            'image': item.get('imageUrl') or item.get('image') or '',
            'passage': item.get('section') or '',
        })
    return questions


def practice_question(request):
    years = [str(y) for y in range(datetime.now().year, 1999, -1)]

    exam = request.GET.get('exam') or ExamType.values[0]
    subject = request.GET.get('subject')
    year = request.GET.get('year') or years[0]

    questions = []
    error_message = None

    if subject:
        if exam in ExamType.values and subject in SubjectType.values and year in years:
            try:
                response = requests.get(
                    ALOC_URL,
                    headers={
                        'X-API-Key': settings.SECRET_KEY},
                    params={'examType': exam, 'subject': subject,
                            'year': year, 'limit': 10},
                    timeout=10,
                )
                if response.status_code == 200:
                    data = response.json().get('data', [])
                    if isinstance(data, dict):
                        data = [data]
                    questions = _normalise(data)
                elif response.status_code == 404:
                    pass  # no questions for this combination; the page says so
                else:
                    error_message = HTTP_MESSAGES.get(
                        response.status_code,
                        'Could not pull questions from the external service.',
                    )
                    if settings.DEBUG:
                        error_message += f' [ALOC {response.status_code}: {response.text[:300]}]'
            except requests.exceptions.RequestException as exc:
                error_message = 'Network problem connecting to the ALOC servers.'
                if settings.DEBUG:
                    error_message += f' [{exc}]'
        else:
            error_message = 'Invalid exam, subject or year selection.'

    context = {
        'mode': 'practice' if questions else 'select',
        'exams': [
            {'slug': e.value, 'name': e.label, 'short': e.short_label}
            for e in ExamType
        ],
        'subjects': [
            {'slug': s.value, 'name': s.label, 'glyph': s.glyph}
            for s in SubjectType
        ],
        'years': [{'value': y} for y in years],
        'selected_exam': exam,
        'questions': questions,
        'subject_name': dict(SubjectType.choices).get(subject, ''),
        'exam_short': ExamType(exam).short_label if exam in ExamType.values else '',
        'year': year,
        'subject_requested': bool(subject),
        'error': error_message,
    }
    return render(request, 'pstque.html', context)
