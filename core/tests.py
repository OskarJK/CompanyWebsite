from django.test import TestCase
from django.urls import reverse
from core.models import CompanyInfo, Category, Service, Post, ContactMessage

# ==========================================
# 1. TESTY WIDOKÓW I STRONY GŁÓWNEJ
# ==========================================
class HomepageTests(TestCase):
    
    def test_homepage_status_code(self):
        """Czy strona główna zwraca poprawny kod HTTP 200?"""
        response = self.client.get(reverse('home')) 
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        """Czy strona główna używa właściwego szablonu HTML?"""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'core/home.html')


# ==========================================
# 2. TESTY MODELI BAZY DANYCH (CRUD & STR)
# ==========================================
class CompanyInfoModelTests(TestCase):

    def test_company_info_creation_and_str(self):
        """Czy dane firmy poprawnie się zapisują i zwracają nazwę firmy?"""
        company = CompanyInfo.objects.create(
            name="Salon Piękna i Urody",
            description="Profesjonalne zabiegi kosmetyczne.",
            street="Musterstraße 12",
            city="Berlin",
            email="salon@beauty.de"
        )
        self.assertEqual(CompanyInfo.objects.count(), 1)
        self.assertEqual(str(company), "Salon Piękna i Urody")


class CategoryModelTests(TestCase):

    def test_category_creation_and_str(self):
        """Czy kategoria poprawnie się zapisuje i zwraca swoją nazwę?"""
        category = Category.objects.create(name="Twarz i Ciało")
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(str(category), "Twarz i Ciało")


class ServiceModelTests(TestCase):

    def test_service_creation_and_str(self):
        """Czy usługa poprawnie wiąże się z kategorią i zwraca swój tytuł?"""
        test_category = Category.objects.create(name="Paznokcie")
        
        service = Service.objects.create(
            title="Manicure Hybrydowy",
            price=120.00,
            description="Piękne i trwałe paznokcie.",
            category=test_category
        )
        self.assertEqual(Service.objects.count(), 1)
        self.assertEqual(str(service), "Manicure Hybrydowy")


class PostModelTests(TestCase):

    def test_post_creation_and_str(self):
        """Czy post (kosmetyki) zapisuje się poprawnie (w tym pole CKEditor)?"""
        post = Post.objects.create(
            title="Ekskluzywne marki z Niemiec",
            description="<p>W naszym salonie używamy tylko certyfikowanych produktów eco.</p>"
        )
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(str(post), "Ekskluzywne marki z Niemiec")
        self.assertIsNotNone(post.created_at)  # Sprawdza czy data utworzenia dodała się automatycznie


# ==========================================
# 3. TESTY FORMULARZA KONTAKTOWEGO (Scenariusze Sukcesu i Błędów)
# ==========================================
class ContactFormTests(TestCase):

    def test_contact_form_submission_success(self):
        """SCENARIUSZ SUKCESU: Wszystkie dane poprawne -> Wiadomość zapisana, status 302"""
        data = {
            'name': 'Jan Kowalski',
            'email': 'jan@kowalski.pl',
            'message': 'Chciałbym zarezerwować termin.',
            'privacy_accepted': 'on'
        }
        response = self.client.post(reverse('home'), data=data)
        
        self.assertEqual(response.status_code, 302)  # Przekierowanie po sukcesie
        self.assertEqual(ContactMessage.objects.count(), 1)
        
        saved_message = ContactMessage.objects.first()
        self.assertEqual(saved_message.status, 'new')  # Domyślny status 'Nowa'
        self.assertTrue(saved_message.privacy_accepted)

    def test_contact_form_missing_privacy_error(self):
        """SCENARIUSZ BŁĘDU: Brak akceptacji polityki prywatności -> Odrzucenie zgłoszenia"""
        data = {
            'name': 'Jan Kowalski',
            'email': 'jan@kowalski.pl',
            'message': 'Chciałbym zarezerwować termin.'
            # 'privacy_accepted' celowo pominięte!
        }
        response = self.client.post(reverse('home'), data=data)
        
        # Baza powinna być pusta, bo formularz nie przeszedł walidacji
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_contact_form_invalid_email_error(self):
        """SCENARIUSZ BŁĘDU: Niepoprawny format adresu e-mail -> Odrzucenie zgłoszenia"""
        data = {
            'name': 'Jan Kowalski',
            'email': 'nie-jestem-emailem',  # Błędny email
            'message': 'Chciałbym zarezerwować termin.',
            'privacy_accepted': 'on'
        }
        response = self.client.post(reverse('home'), data=data)
        
        # Formularz powinien wykryć zły email i nie zapisywać rekordu
        self.assertEqual(ContactMessage.objects.count(), 0)