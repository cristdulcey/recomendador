from django.contrib import admin

# Register your models here.
from companies.models import Company, BranchCompany, BranchServices, Qualification


@admin.register(Company)
class AdmniCompany(admin.ModelAdmin):
    pass

@admin.register(BranchCompany)
class AdmniBranchCompany(admin.ModelAdmin):
    pass

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