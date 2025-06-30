from django.contrib import admin
from .models import Ticket
# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title", {"fields": ["title"]}),
        ("Description", {"fields": ["description"]}),
        ("Status", {"fields": ["status"]}),
        ("User/Date", {"fields": ["creator", "creation_date"]}),
    ]

admin.site.register(Ticket, TicketAdmin)