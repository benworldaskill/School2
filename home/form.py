from django import forms
from .models import Enquiry, Apply


class EnquiryForm(forms.ModelForm):

    class Meta:
        model = Enquiry

        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "student_first_name",
            "student_last_name",
            "student_age",
            "gender",
            "details",
        ]

        widgets = {

            # Parent
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "First Name"
            }),

            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Last Name"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email Address"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone Number"
            }),

            # Student
            "student_first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Student First Name"
            }),

            "student_last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Student Last Name"
            }),

            "student_age": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "gender": forms.Select(attrs={
                "class": "form-select"
            }),

            # Enquiry
            "details": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Tell us about your enquiry",
                "rows": 5
            }),
        }


class ApplyForm(forms.ModelForm):

    class Meta:
        model = Apply
        fields = [
            "student_name",
            "student_lastname",
            "student_email",
            "date_of_birth",
            "place_of_birth",
            "language_spoken_at_home",
            "nationality",
            "state_of_origin",
            "gender",
            "height",
            "weight",
            "family_size",
            "name_of_last_school",
            "last_school_startdate",
            "last_school_enddate",
            "position_in_last_school",
            "reason_for_leaving",
            "class_expexting_admission",
            "transport_service",
            "any_certificate",
            "vision",
            "hearing",
            "speech",
            "general_vitality",
            "disability",
            "father_title",
            "father_name",
            "occupation",
            "office_address",
            "home_address",
            "father_phone",
            "father_email",

            # mother
            "mother_title",
            "mother_name",
            "mo_occupation",
            "mo_office_address",
            "mo_home_address",
            "mother_phone",
            "mother_email",

            # GD
            "gd_title",
            "gd_name",
            "gd_occupation",
            "gd_office_address",
            "gd_home_address",
            "gd_phone",
            "gd_email"

        ]

        widgets = {
            # Student
            "student_name": forms.TextInput(attrs={
                "class": "form-control",

            }),

            "student_lastname": forms.TextInput(attrs={
                "class": "form-control",

            }),

            "student_email": forms.EmailInput(attrs={
                "class": "form-control",

            }),

            "date_of_birth": forms.TextInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            # Student
            "place_of_birth": forms.TextInput(attrs={
                "class": "form-control",

            }),

            "language_spoken_at_home": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "nationality": forms.TextInput(attrs={
                "class": "form-control",

            }),
            "state_of_origin": forms.Select(attrs={
                "class": "form-select"
            }),

            "gender": forms.Select(attrs={
                "class": "form-select"
            }),

            "height": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "weight": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "family_size": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "name_of_last_school": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "last_school_startdate": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "last_school_enddate": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "position_in_last_school": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "reason_for_leaving": forms.TextInput(attrs={
                "class": "form-control",

                "rows": 3

            }),

            "class_expexting_admission": forms.TextInput(attrs={
                "class": "form-control",

            }),



            "transport_service": forms.Select(attrs={
                "class": "form-select",

            }),

            "any_certificate": forms.TextInput(attrs={
                "class": "form-control",


            }),

            # Medical Report Section
            "vision": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "hearing": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "speech": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "general_vitality": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "disability": forms.TextInput(attrs={
                "class": "form-control",


            }),

            # Parent Details(FATHER)
            "father_title": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "father_name": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "occupation": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "office_address": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "home_address": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "father_phone": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "father_email": forms.TextInput(attrs={
                "class": "form-control",


            }),

            # Parent Details(MOTHER)
            "mother_title": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "mother_name": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "mo_occupation": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "mo_office_address": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "mo_home_address": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "mother_phone": forms.TextInput(attrs={
                "class": "form-control",

            }),

            "mother_email": forms.TextInput(attrs={
                "class": "form-control",


            }),

            # Guardian Details
            "gd_title": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "gd_name": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "gd_occupation": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "gd_office_address": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "gd_home_address": forms.TextInput(attrs={
                "class": "form-control",


            }),

            "gd_phone": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "gd_email": forms.TextInput(attrs={
                "class": "form-control",
            }),
        }
