from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class CompanyInfo(models.Model):
    # Dane firmy
    name = models.CharField(max_length=100, verbose_name="Nazwa firmy")
    description = models.TextField(verbose_name="Opis firmy")
    logo = models.ImageField(upload_to='company/', verbose_name="Logo firmy", blank=True, null=True)
    
    # Dane kontaktowe i prawne (ważne dla rynku niemieckiego)
    address = models.TextField(verbose_name="Adres")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    email = models.EmailField(verbose_name="Email kontaktowy")
    ust_id = models.CharField(max_length=50, verbose_name="USt-IdNr (NIP)", blank=True, null=True)
    ust_id_information = models.TextField(verbose_name="Informacje o USt-IdNr (NIP)", blank=True, null=True)
    
    # Social Media
    facebook_url = models.URLField(blank=True, null=True, verbose_name="Link do Facebooka")
    instagram_url = models.URLField(blank=True, null=True, verbose_name="Link do Instagrama")
    whatsapp_url = models.URLField(blank=True, null=True, verbose_name="Link do WhatsApp")
    treatwell_url = models.URLField(blank=True, null=True, verbose_name="Link do Treatwell")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Dane firmy"
        verbose_name_plural = "Dane firmy"
        
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa kategorii")

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

    def __str__(self):
        return self.name
    
class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nazwa usługi")
    description = models.TextField(verbose_name="Opis zabiegu")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Cena (€)")
    image = models.ImageField(upload_to='services/', verbose_name="Zdjęcie usługi", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoria", null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Usługa"
        verbose_name_plural = "Usługi"

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tytuł posta")
    description = CKEditor5Field('Opis', config_name='extends')
    image = models.ImageField(upload_to='treatments/', verbose_name="Zdjęcie", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data utworzenia posta")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posty"
        
CONTACTMESSAGE_STATUS_CHOICES = [
    ('new', 'Nowa'),
    ('in_progress', 'W trakcie realizacji'),
    ('closed', 'Zamknięta'),    
]
class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Imię")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Wiadomość")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data wysłania")
    status = models.CharField(max_length=20, choices=CONTACTMESSAGE_STATUS_CHOICES, default='new', verbose_name="Status wiadomości")

    def __str__(self):
        return f"Wiadomość od {self.name}"

    class Meta:
        verbose_name = "Formularz kontaktowy"
        verbose_name_plural = "Zgłoszenia z formularza kontaktowego"