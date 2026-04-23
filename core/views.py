from django.shortcuts import render

# Create your views here.
from .models import CompanyInfo, Service, Post

def home(request):
    # Pobieramy dane z bazy
    company = CompanyInfo.objects.first() # Zakładamy, że masz jeden rekord z danymi firmy
    services = Service.objects.all()
    posts = Post.objects.all().order_by('-created_at') # Najnowsze posty pierwsze
    
    context = {
        'company': company,
        'services': services,
        'posts': posts,
    }
    return render(request, 'core/home.html', context)