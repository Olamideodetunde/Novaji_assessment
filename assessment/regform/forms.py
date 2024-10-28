from datetime import date
from django import forms
from .models import User
class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['fname','lname','email','tel_phone','pwd','date_of_birth']
        widgets={
            'fname':forms.TextInput(attrs={'required':'True'}),
            'lname':forms.TextInput(attrs={'required':'True'}),
            'email':forms.EmailInput(attrs={'required':'True'}),
            'tel_phone':forms.TextInput(attrs={'max_length':'11','min_length':'11','pattern':'[0/9]11+'}),
            'pwd':forms.PasswordInput(attrs={'required':'True','min_length':'8','pattern':'[A]+[a]+[0/9]+[@]+'}),
            'date_of_birth':forms.DateInput(attrs={'required':'True','type':'date'}),
        }
    
        
        