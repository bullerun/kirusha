from django.contrib import admin

# Register your models here.
from .models import *

class twoFactorAuthenticationAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'time_create', 'photo', 'is_authentication')
    list_display_links = ('id', 'login')
    search_fields = ('login', 'time_create')
    list_editable = ('is_authentication', )
    list_filter = ('is_authentication', 'time_create')


admin.site.register(twoFactorAuthentication, twoFactorAuthenticationAdmin)