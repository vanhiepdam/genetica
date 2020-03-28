from django.contrib import admin

from genetica.specimens.models import Specimen, TestStep


class SpecimenAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = []


admin.site.register(Specimen, SpecimenAdmin)
admin.site.register(TestStep, SpecimenAdmin)
