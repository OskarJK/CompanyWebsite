from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from core.forms import ContactForm

# Create your views here.
from .models import CompanyInfo, ContactMessage, Service, Post, Category

def home(request):
    # 1. Obsługa wysyłania formularza (POST)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        is_privacy_accepted = request.POST.get('privacy_accepted') == 'on'
        
        if form.is_valid() and is_privacy_accepted:
            contact = form.save(commit=False)
            contact.privacy_accepted = True
            contact.save()

            # WYSYŁANIE MAILA PRZEZ GMAIL
            # Wyciągamy bezpiecznie oczyszczone dane z formularza
            user_name = form.cleaned_data.get('name', 'Nie podano')
            user_email = form.cleaned_data.get('email', 'Nie podano')
            user_message = form.cleaned_data.get('message', '')
            
            # Formatujemy treść wiadomości e-mail
            subject = f"Nowa wiadomość od {user_name} (Salon Kosmetyczny)"
            
            # Zapasowa treść tekstowa:
            full_message = f"Otrzymałeś nową wiadomość z formularza kontaktowego strony.\n\n" \
                           f"Od: {user_name}\n" \
                           f"E-mail klienta: {user_email}\n\n" \
                           f"Treść wiadomości:\n{user_message}"
                           
            # HTMLowa treść wiadomości (bardziej atrakcyjna wizualnie)
            html_message = f"""
                        <div style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e8e2de; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
                            
                            <div style="background-color: #f7ede8; padding: 25px; text-align: center; border-bottom: 2px solid #e3d3ca;">
                                <h2 style="color: #4a3e3d; margin: 0; font-size: 22px; font-weight: 500; letter-spacing: 0.5px;">Nowe zgłoszenie z formularza</h2>
                                <p style="color: #8a7a78; margin: 5px 0 0 0; font-size: 14px;">Strona internetowa Twojego Salonu</p>
                            </div>
                            
                            <div style="padding: 30px; background-color: #ffffff;">
                                <table style="width: 100%; border-collapse: collapse; margin-bottom: 25px;">
                                    <tr>
                                        <td style="padding: 12px 0; border-bottom: 1px solid #f5f0ed; color: #8a7a78; font-size: 14px; width: 30%;"><strong>Klient:</strong></td>
                                        <td style="padding: 12px 0; border-bottom: 1px solid #f5f0ed; color: #332d2c; font-size: 15px;">{user_name}</td>
                                    </tr>
                                    <tr>
                                        <td style="padding: 12px 0; border-bottom: 1px solid #f5f0ed; color: #8a7a78; font-size: 14px;"><strong>Adres e-mail:</strong></td>
                                        <td style="padding: 12px 0; border-bottom: 1px solid #f5f0ed; font-size: 15px;">
                                            <a href="mailto:{user_email}" style="color: #b58d78; text-decoration: none; font-weight: bold;">{user_email}</a>
                                        </td>
                                    </tr>
                                </table>
                                
                                <div style="background-color: #faf8f7; border-left: 4px solid #d4beab; padding: 20px; border-radius: 4px;">
                                    <h4 style="color: #4a3e3d; margin: 0 0 10px 0; font-size: 14px; text-transform: uppercase; letter-spacing: 0.5px;">Treść wiadomości:</h4>
                                    <p style="color: #5c504e; line-height: 1.6; margin: 0; font-size: 15px; white-space: pre-wrap;">{user_message}</p>
                                </div>
                            </div>
                            
                            <div style="background-color: #faf8f7; padding: 15px; text-align: center; font-size: 11px; color: #a19290; border-top: 1px solid #e8e2de;">
                                Ta wiadomość została wysłana automatycznie przez system CMS Twojej strony www.
                            </div>
                        </div>
                        """
            
            try:
                send_mail(
                    subject=subject,
                    message=full_message,
                    html_message=html_message,  # Dodajemy HTMLową wiadomość
                    from_email=settings.DEFAULT_FROM_EMAIL,  # Twój Gmail z .env jako nadawca
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],  # Odbiorca (również Twój mail)
                    fail_silently=False,
                )
            except Exception as e:
                # Łapiemy ewentualny błąd serwera poczty w konsoli (np. brak sieci), 
                # aby strona nie wywaliła błędu 500 użytkownikowi końcowemu.
                print(f"Błąd wysyłania maila przez SMTP: {e}")
            # --------------------------------------------
            messages.success(request, "Dziękujemy! Twoja wiadomość została wysłana pomyślnie.")
            return redirect('home') # Sukces -> pełne odświeżenie i czysty formularz
        
        # Jeśli są błędy (np. zły mail), kod przechodzi dalej. 
        # NIE ROBIMY przekierowania (redirect), dzięki czemu błędy i wpisany tekst zostają w formularzu!
        
    else:
        # 2. Pierwsze wejście na stronę (GET) - pusty formularz
        form = ContactForm()
        
    # Pobieramy dane z bazy
    company = CompanyInfo.objects.first() # Zakładamy, że masz jeden rekord z danymi firmy
    services = Service.objects.all()
    categories = Category.objects.prefetch_related('services').all()
    posts = Post.objects.all().order_by('-created_at') # Najnowsze posty pierwsze
    
    context = {
        'company': company,
        'services': services,
        'categories': categories,
        'posts': posts,
        'form': form,
    }
    return render(request, 'core/home.html', context)