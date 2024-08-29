from django import forms
from home.models import Email


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['mail']
        widgets = {
            'mail': forms.TextInput(attrs={'class': 'form-control', "autocomplete": "off", "placeholder": "Enter your email.."})
        }
