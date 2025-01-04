from django import forms

from web.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ()
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your name:"}
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control required email",
                    "placeholder": "Your Mail:",
                }
            ),
            "number": forms.TextInput(
                attrs={
                    "class": "form-control required number-input",
                    "placeholder": "Enter Your Phone Number:",
                }
            ),
            "subject": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your subject:"}
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control required",
                    "rows": 5,
                    "placeholder": "Your Message:",
                }
            ),
        }
