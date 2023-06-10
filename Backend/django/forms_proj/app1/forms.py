from django import forms
from django.core import validators

def name_camel_cased(value):
    for i in value.split(" "):
        if i[0] < 'A' or i[0] > 'Z':
            raise forms.ValidationError("Name should be camel cased")


class BasicForm(forms.Form):
    name = forms.CharField(validators=[name_camel_cased])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter the Email ID again:')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
    
    def clean(self):
        data = super().clean()
        email = data['email']
        vemail = data['verify_email']
        if email  != vemail:
            raise forms.ValidationError("The emails must match!!")
    

    # BUT WILL ALWAYS USE DJANGO'S INBUILT VALIDATORS
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher):
    #         raise forms.ValidationError("Bot Caught!!")
    #     return botcatcher