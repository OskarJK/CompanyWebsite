from django.contrib import admin
from .models import Category, CompanyInfo, Service, Post, ContactMessage

# Register your models here.

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'ust_id',]
    # Ograniczenie do jednego rekordu, żeby admin nie stworzył 10 firm
    def has_add_permission(self, request):
        return not CompanyInfo.objects.exists()
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'title', 'price', 'category']
    list_filter = ['category']
    list_editable = ['order']
    ordering = ['order']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'created_at', 'status', 'privacy_accepted']
    list_filter = ['created_at', 'status', 'privacy_accepted']
    
    #Blokada edycji wiadomości
    def get_readonly_fields(self, request, obj=None):
            if obj:
                return ['name', 'email', 'message', 'created_at', 'privacy_accepted',] 
            return []
    #Blokada dodawania nowych wiadomości przez admina
    def has_add_permission(self, request):
            return False

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at',]
    list_filter = ['created_at',]
    
    def has_add_permission(self, request):
        # Pozwól dodać tylko wtedy, gdy w bazie jest 0 postów
        return Post.objects.count() == 0
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name']
    list_editable = ['order']
    ordering = ['order']
    

