from django.contrib import admin

# Register your models here.
from companies.models import Company, BranchCompany, BranchServices, Qualification

class BranchCompanyInline(admin.StackedInline):
    model = BranchCompany
    extra = 0
    raw_id_fields = ("company", "supervisor", "city")

class BranchServicesInline(admin.StackedInline):
    model = BranchServices
    extra = 0
    raw_id_fields = ("services", "branch_company")


@admin.register(Company)
class AdminCompany(admin.ModelAdmin):
    list_display = ("nit", "name", "site",)
    list_display_links = ("nit", "name", "site",)
    search_fields = ("nit", "name",)
    list_filter = ("name", )
    inlines = [BranchCompanyInline]

@admin.register(BranchCompany)
class AdmniBranchCompany(admin.ModelAdmin):
    list_display = ("company", "city", "address", "geolocation")
    list_display_links = ("company", "city", "address",)
    search_fields = ("city", "company",)
    list_filter = ("supervisor",)
    inlines = [BranchServicesInline]

class QualificationInlines(admin.StackedInline):
    model = Qualification
    extra = 0

@admin.register(BranchServices)
class AdmniBranchServices(admin.ModelAdmin):
    list_display = ("services", "branch_company", "price")
    list_display_links = ("services", "branch_company", "price")
    raw_id_fields = ("services", "branch_company")
    search_fields = ("price", "services")
    list_filter = ("price", "services")
    inlines = (QualificationInlines,)

@admin.register(Qualification)
class AdmniQualification(admin.ModelAdmin):
    list_display = ("client", "comment", "score")
    list_display_links = ("client", "comment", "score")
    raw_id_fields = ("client", "branch_services")
    search_fields = ("client", "score")
    list_filter = ("comment", "score")
    #inlines = (NotificationInline,),