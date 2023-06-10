from app1.models import User
from django import forms


class SignUp(forms.ModelForm):
    class Meta:
        model = User
        fields = ("name","email","text")
        widgets = {
            'text' : forms.Textarea(attrs={'cols': 80, 'rows': 10})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        for i in name.lower():
            if (i < 'a' or i > 'z'):
                raise forms.ValidationError("Name should be alphabetical only")
        return name



            
    

