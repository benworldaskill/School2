from django.shortcuts import render, redirect
from .form import EnquiryForm, ApplyForm
from .models import Stories, Gallery
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail

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
