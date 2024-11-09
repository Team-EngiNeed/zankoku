# engineed/forms.py

from django import forms

class LoginForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100)
    grade_section = forms.CharField(label='Grade & Section', max_length=50)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
