from django.contrib import admin
from contact_us.models import Contact
import datetime


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'interest', 'application_date')
    
admin.site.register(Contact, ContactAdmin)
