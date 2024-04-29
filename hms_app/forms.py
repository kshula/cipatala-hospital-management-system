# forms.py
from django import forms
from .models import Patient

class ReceptionistLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'first_name', 'last_name', 'date_of_birth',  
            'insurance_provider',  
            'payment_method', 'preferred_language', 'religious_preferences',
            'reason_for_visit', 'referring_physician', 
            # Add other fields as needed
        ]