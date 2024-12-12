from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Plant,PlantCategory
class Regform(UserCreationForm):
    username= forms.CharField(widget=forms.TextInput(
        attrs= {'placeholder':'Enter your username',
                'class':'form-control'
                }))
    email= forms.CharField(widget=forms.EmailInput(
        attrs= {'placeholder':'Enter your email',
                'class':'form-control'
                }))
    password1= forms.CharField(widget=forms.PasswordInput(
        attrs= {'placeholder':'Enter your password',
                'class':'form-control'
                }))
    password2= forms.CharField(widget=forms.PasswordInput(
        attrs= {'placeholder':'Enter your password again',
                'class':'form-control'
                }))
    first_name= forms.CharField(widget=forms.TextInput(
        attrs= {'placeholder':'Enter your firstname ',
                'class':'form-control'
                }))
    last_name= forms.CharField(widget=forms.TextInput(
        attrs= {'placeholder':'Enter your lastname ',
                'class':'form-control'
                }))

    class Meta:
        model=User
        fields=['username','first_name','last_name']

