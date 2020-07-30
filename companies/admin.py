from django.contrib import admin

# Register your models here.
from companies.models import Company, BranchCompany, BranchServices, Qualification


@admin.register(Company)
class AdmniCompany(admin.ModelAdmin):
    pass

@admin.register(BranchCompany)
class AdmniBranchCompany(admin.ModelAdmin):
    pass

@admin.register(BranchServices)
class AdmniBranchCompany(admin.ModelAdmin):
    pass

@admin.register(Qualification)
class AdmniQualification(admin.ModelAdmin):
    pass