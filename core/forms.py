from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Twoje imię', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Twój adres e-mail', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Twoja wiadomość', 'class': 'form-control', 'rows': 5}),
        }