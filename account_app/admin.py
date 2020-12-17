from django.contrib import admin
from account_app import models

# Admin header change
admin.site.site_header = "Get PS5"


class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'avatar_tag', 'name', 'is_seller', 'is_staff', 'is_active', 'is_ban', 'is_delete',)
    list_filter = (['is_seller', 'is_staff', 'is_active', 'is_ban', 'is_delete', 'gender', 'created'])
    search_fields = ('email', 'name')
    ordering = ['-is_seller', '-is_staff', '-is_active', '-is_ban', ]
    # prepopulated_fields = {'email': ('name',)}


admin.site.register(models.User, AccountAdmin)
