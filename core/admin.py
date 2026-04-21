from django.contrib import admin
from .models import CompanyInfo, Service, Post, ContactMessage

# Register your models here.

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'ust_id',]
    # Ograniczenie do jednego rekordu, żeby admin nie stworzył 10 firm
    def has_add_permission(self, request):
        return not CompanyInfo.objects.exists()
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price',]

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at',]
    list_filter = ['created_at']
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at',]
    list_filter = ['created_at',]
