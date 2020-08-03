from django.contrib import admin

from companies.models import Qualification, BranchCompany
from persons.models import Client, Supervisor, City


# Register your models here.


class QualificationInlines(admin.StackedInline):
    model = Qualification
    extra = 0

class ClientInlines(admin.StackedInline):
    model = Client
    extra = 0

class BranchCompanyInlines(admin.StackedInline):
    model =BranchCompany
    extra = 0

@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    list_display = ("user", "phone")
    list_display_links = ("user", "phone")
    raw_id_fields = ("user", "city")
    search_fields = ("phone", "address")
    list_filter = ("user",)
    inlines =(QualificationInlines,)


@admin.register(Supervisor)
class AdminSupervisor(admin.ModelAdmin):
    list_display = ("user", "phone")
    list_display_links = ("user", "phone")
    raw_id_fields = ("user",)
    search_fields = ("phone",)
    list_filter = ("user",)
    inlines = (BranchCompanyInlines,)


@admin.register(City)
class AdminCity(admin.ModelAdmin):
    list_display = ("name", "department")
    list_display_links = ("name", "department")
    search_fields = ("name",)
    list_filter = ("name",)
    inlines = (BranchCompanyInlines, ClientInlines,)
