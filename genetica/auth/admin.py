from django.contrib import admin

from genetica.auth.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'username', 'email'
    ]
    readonly_fields = []


admin.site.register(User, UserAdmin)
