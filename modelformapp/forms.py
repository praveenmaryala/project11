from django import forms
from .models import Reg

class RegForm(forms.ModelForm):
    class Meta:
        model=Reg
        fields=['username','password','conf_password','first_name','last_name','email','mobileno']
        widgets={'password':forms.PasswordInput(),
                 'conf_password':forms.PasswordInput()}
class LoginForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput())