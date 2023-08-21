from django.forms import ModelForm,PasswordInput,TextInput
from . import models

class UserForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['username','first_name','last_name','email','password']
        widgets = {'password': PasswordInput()}
        label = {'username': 'Enter a valid username',
                 'first_name': 'Enter your first name',
                 'last_name': 'Enter your last name'}
        
        
class UserProfileForm(ModelForm):
    class Meta:
        model = models.UserProfile
        fields = ['level','picture']
        