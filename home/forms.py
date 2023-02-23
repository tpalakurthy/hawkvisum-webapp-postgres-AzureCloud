from django import forms

# Create your forms here.

class ContactForm(forms.Form):
    customer_name = forms.CharField(max_length=50)
    customer_email = forms.EmailField(max_length=150)
    customer_subject = forms.CharField(max_length=200)
    customer_message = forms.CharField(max_length=2000)

class CareersForm(forms.Form):
    applicant_name = forms.CharField(max_length=50)
    applicant_email = forms.EmailField(max_length=150)
    applicant_subject = forms.CharField(max_length=200)
    applicant_position = forms.CharField(max_length=200)
    applicant_message = forms.CharField(max_length=2000)
    applicant_resume = forms.FileField()