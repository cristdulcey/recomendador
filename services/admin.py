from django.contrib import admin
from .models import Service, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('parent', 'name',)
    list_display_links = ('name',)
    raw_id_fields = ("parent",)
    list_filter = ('parent', )
    search_fields = ('name', )
    list_per_page = 10


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('category', 'name',)
    list_display_links = ('name',)
    list_filter = ('category',)
    search_fields = ('name', 'category__name', )
    list_per_page = 10

admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)