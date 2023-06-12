from django import forms

def username_validator(value):
    if ' ' in value:
        raise forms.ValidationError("username shouldn't have space in between")
    return value

class LoginPage(forms.Form):
    username = forms.CharField(max_length=256,validators=[username_validator])
    email = forms.EmailField()
    verify_email = forms.EmailField()

    def clean(self):
        data = self.cleaned_data
        if data['email'] != data['verify_email']:
            raise forms.ValidationError("Both the emails must match")
        return data
