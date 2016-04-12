from django.contrib import admin

from backup.models import Contact


class ContactAdmin(admin.ModelAdmin):
    can_delete = False
    list_per_page = 50
    list_display = (
        'name', 'phone_home', 'phone_work', 'email_home', 'email_work')
    list_display_links = (
        'name', 'phone_home', 'phone_work', 'email_home', 'email_work')
    site_title = 'Ok'


admin.site.register(Contact, ContactAdmin)
