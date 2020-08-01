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
    list_display = ("company", "city", "address",)
    list_display_links = ("company", "city", "address",)
    search_fields = ("city", "company",)
    list_filter = ("supervisor",)
    inlines = [BranchServicesInline]

@admin.register(BranchServices)
class AdmniBranchServices(admin.ModelAdmin):
    pass

@admin.register(Qualification)
class AdmniQualification(admin.ModelAdmin):
    pass