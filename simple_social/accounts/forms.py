from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    
    class Meta:
        
        model = get_user_model
        fields = ('username','email','password1','password2')
        labels = {
            'username' : 'Given Name',
            'email' : 'Enter the Email ID'
        }