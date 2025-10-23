from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import CustomUser
from django import forms
class SignUpForm(UserCreationForm):
    role_choice=(('student','student'),('teacher','teacher'))
    role=forms.ChoiceField(choices=role_choice)
    gender_choice=(('male','male'),('female','female'))
    gender=forms.ChoiceField(choices=gender_choice,widget=forms.RadioSelect)
    class Meta:
        model=CustomUser
        fields=('first_name','last_name','phone','role','gender','username','email','password1')

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class OTPForm(forms.Form):
    otp=forms.CharField()
