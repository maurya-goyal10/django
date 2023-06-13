from django import forms
from basic_app.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ['username','first_name','last_name','email','password']

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ['message','profile_pic'] 