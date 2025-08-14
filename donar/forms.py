from django import forms
from .models import*

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = PatientRegistration  
        fields = '__all__'  

class DonarRegistrationForm(forms.ModelForm):
    class Meta:
        model = DonarRegistration  
        fields = '__all__'  