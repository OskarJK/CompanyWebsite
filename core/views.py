from django.shortcuts import render

from core.forms import ContactForm
from django.shortcuts import render, redirect

# Create your views here.
from .models import CompanyInfo, ContactMessage, Service, Post

def home(request):
    # Formularz kontaktowy
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') # Odświeża stronę po wysłaniu
    else:
        form = ContactForm()
        
    # Pobieramy dane z bazy
    company = CompanyInfo.objects.first() # Zakładamy, że masz jeden rekord z danymi firmy
    services = Service.objects.all()
    posts = Post.objects.all().order_by('-created_at') # Najnowsze posty pierwsze
    contact_messages = ContactMessage.objects.all().order_by('-created_at')
    
    context = {
        'company': company,
        'services': services,
        'posts': posts,
        'contact_messages': contact_messages,
        'form': form,
    }
    return render(request, 'core/home.html', context)