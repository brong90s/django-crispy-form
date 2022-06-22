# core/forms.py

from django import forms

class BasicForm(forms.Form):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDERS)
    phone_number = forms.CharField(label='Phone')
    about_you = forms.CharField(widget=forms.Textarea())
