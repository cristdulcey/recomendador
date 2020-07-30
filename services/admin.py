from django.contrib import admin

# Register your models here.
from services.models import Category, Services


@admin.register(Category)
class AdmniCategory(admin.ModelAdmin):
    pass

@admin.register(Services)
class AdmniServices(admin.ModelAdmin):
    pass