from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'is_active')
    search_fields = ('name', 'email')
    list_filter = ('country', 'is_active')
