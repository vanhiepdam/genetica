from django.contrib import admin

from genetica.reports.models import TraitTemplate, Trait, Report


class TemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'level']


class ReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = []


admin.site.register(TraitTemplate, TemplateAdmin)
admin.site.register(Trait, ReportAdmin)
admin.site.register(Report, ReportAdmin)
