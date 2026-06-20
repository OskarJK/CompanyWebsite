from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    privacy_accepted = forms.BooleanField(
        required=True,
        error_messages={'required': 'Sie müssen die Datenschutzbestimmungen akzeptieren.'}
    )
    
    #Honeypot
    website = forms.CharField(required=False, widget=forms.HiddenInput())
    
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message', 'privacy_accepted']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Dein Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Deine E-Mail-Adresse'}),
            'message': forms.Textarea(attrs={'placeholder': 'Deine Nachricht', 'rows': 5}),
        }
    def clean_website(self):
        # Jeśli pole "website" jest wypełnione - to bot
        website = self.cleaned_data.get('website')
        if website:
            raise forms.ValidationError("Spam wykryty.")
        return website
        