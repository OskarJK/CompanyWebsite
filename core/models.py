from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class CompanyInfo(models.Model):
    
    # Dane firmy
    name = models.CharField(max_length=100, verbose_name="Nazwa firmy")
    name_additional = models.CharField(max_length=100, verbose_name="Dodatkowa nazwa firmy (np.Kosmetiksalon)", blank=True, null=True)
    motto = models.CharField(max_length=200, verbose_name="Motto firmy", blank=True, null=True)
    owner_name = models.CharField(max_length=100, verbose_name="Imię właściciela", blank=True, null=True)
    description = models.TextField(verbose_name="Opis firmy")
    logo = models.ImageField(upload_to='company/', verbose_name="Logo firmy - nie używane", blank=True, null=True)
    
    # Dane kontaktowe i prawne (ważne dla rynku niemieckiego)
    street = models.CharField(max_length=100, verbose_name="Ulica", blank=True, null=True)
    postal_code = models.CharField(max_length=20, verbose_name="Kod pocztowy", blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name="Miasto", blank=True, null=True)
    country = models.CharField(max_length=100, verbose_name="Kraj", blank=True, null=True)
    phone = models.CharField(max_length=30, verbose_name="Telefon", blank=True, null=True)
    email = models.EmailField(verbose_name="Adres e-mail", blank=True, null=True)
    
    # Obowiązkowe w niemieckim Impressum!
    ust_id = models.CharField(max_length=50, verbose_name="USt-IdNr (NIP) - nieobowiązkowe do wpisania", blank=True, null=True)
    
    ust_id_information = models.TextField(verbose_name="Umsatzsteuer", blank=True, null=True)
    
    eu_streitschlichtung = models.TextField(
        verbose_name="Rozstrzyganie sporów w UE (EU-Streitschlichtung)",
        blank=True,
        null=True
    )
    
    odr_link = models.URLField(
        default="https://ec.europa.eu/consumers/odr/", 
        verbose_name="Link do platformy ODR (wyszczególniony w prawie UE)"
    )
    
    liability_contents = models.TextField(verbose_name="Odpowiedzialność za treści (Haftung für Inhalte)", blank=True, null=True)
    
    liability_links = models.TextField(verbose_name="Odpowiedzialność za linki (Haftung für Links)", blank=True, null=True)
    
    # Sekcje Polityki Prywatności (Datenschutz)
    privacy_intro = models.TextField(
        verbose_name="Polityka prywatności - Wstęp (Einleitung und Überblick)", 
        blank=True, 
        null=True
    )
    privacy_purposes = models.TextField(
        verbose_name="Polityka prywatności - Cele (Zweck der Datenverarbeitung)", 
        blank=True, 
        null=True
    )
    privacy_legal_grounds = models.TextField(
        verbose_name="Polityka prywatności - Podstawy prawne (Rechtsgrundlagen)", 
        blank=True, 
        null=True
    )
    privacy_third_parties = models.TextField(
        verbose_name="Polityka prywatności - Przekazywanie danych (Datenübermittlung an Dritte)", 
        blank=True, 
        null=True
    )

    
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
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Kategoria", blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Usługa"
        verbose_name_plural = "Usługi"
        ordering = ['category']

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nazwa kosmetyków których używamy")
    description = CKEditor5Field('Opis', config_name='extends')
    image = models.ImageField(upload_to='treatments/', verbose_name="Zdjęcie kosmetyków", blank=True, null=True)
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
    privacy_accepted = models.BooleanField(
        default=False, 
        verbose_name="Zaakceptowano politykę prywatności (Datenschutz)"
    )

    def __str__(self):
        return f"Wiadomość od {self.name}"

    class Meta:
        verbose_name = "Formularz kontaktowy"
        verbose_name_plural = "Zgłoszenia z formularza kontaktowego"
        ordering = ['-created_at']