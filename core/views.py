from django.shortcuts import render

from core.forms import ContactForm
from django.shortcuts import render, redirect

# Create your views here.
from .models import CompanyInfo, ContactMessage, Service, Post, Category

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