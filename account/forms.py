from django.contrib.auth.models import User 
from .models import Profile
from django import forms
from django.forms import ModelForm


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class UserRegistrationForm(ModelForm):
    password  = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields  = ('username', 'first_name', 'email')
    
    def clean_password2(self):
        cd  = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Password don't match.")
        return cd['password2']

class ProfileEditForms(ModelForm):
    class Meta:
        model = Profile 
        fields = ['date_of_birth','photo']

class UserEditForm(ModelForm):
    class Meta: 
        model = User 
        fields = ['username','first_name','last_name', 'email']
