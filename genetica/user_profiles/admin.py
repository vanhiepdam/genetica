from django.contrib import admin

from genetica.user_profiles.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(UserProfile, UserProfileAdmin)
