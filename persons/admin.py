from django.contrib import admin

from persons.models import Client, Supervisor, City


# Register your models here.

@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    pass

@admin.register(Supervisor)
class AdminSupervisor(admin.ModelAdmin):
    pass

@admin.register(City)
class AdminCity(admin.ModelAdmin):
    pass