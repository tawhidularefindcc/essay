# dappx/forms.py
from django import forms
from dappx.models import UserProfileInfo, SubmissionForm
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        help_texts = {
            'username': None,
        }
        fields = ('username', 'password', 'email')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('Name', 'contact_number', 'State', 'Country', 'DOB')


class SubmissionForm(forms.ModelForm):
    title = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'col-751'}))
    essay = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'class': 'col-752'}))

    class Meta():
        model = SubmissionForm
        fields = ('title', 'essay')

