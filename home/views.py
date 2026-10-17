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

    
    exam = request.GET.get('exam') or 'jamb'
    subject = request.GET.get('subject')
    year = request.GET.get('year') or years[0]

    questions = []
    error_message = None

    
    try:
        valid_exams = [e.value for e in ExamType]
        valid_subjects = [s.value for s in SubjectType]
    except AttributeError:

        valid_exams = []
        valid_subjects = []

    if subject:
        if exam in valid_exams and subject in valid_subjects and year in years:
            try:
                response = requests.get(
                    ALOC_URL,
                    headers={'X-API-Key': settings.SECRET_KEY},
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
                    pass
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
            {'slug': getattr(e, 'value', str(e)), 'name': getattr(
                e, 'label', str(e)), 'short': getattr(e, 'short_label', str(e))}
            for e in ExamType
        ],
        'subjects': [
            {'slug': getattr(s, 'value', str(s)), 'name': getattr(
                s, 'label', str(s)), 'glyph': getattr(s, 'glyph', '')}
            for s in SubjectType
        ],
        'years': [{'value': y} for y in years],
        'selected_exam': exam,
        'questions': questions,
        'subject_name': dict(getattr(SubjectType, 'choices', [])).get(subject, ''),
        'exam_short': getattr(ExamType(exam), 'short_label', '') if exam in valid_exams else '',
        'year': year,
        'subject_requested': bool(subject),
        'error': error_message,
    }
    return render(request, 'pstque.html', context)
