# core/forms.py

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('first_name', css_class='form-group col-4'),
                Div('last_name', css_class='form-group col-4'),
                Div('email', css_class='form-group col-4'),
                css_class='form-row'
            ),
            Div(
                Div('password', css_class='form-group col-4'),
                Div('confirm_password', css_class='form-group col-4'),
                css_class='form_row'
            ),
            Div(
                Div('gender', css_class='form-group col-4'),
                Div('phone_number', css_class='form-group col-8'),
                css_class='form-row'
            ),
            'about_you',
            Submit('submit', 'Sign Up', css_class='mt-4')
        )
