from django.contrib import admin

from genetica.services.models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = []


admin.site.register(Service)
