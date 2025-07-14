from django.contrib import admin
from .models import Ticket
# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    list_filter = ["archived"]
    list_display = ('title', 'creator', 'creation_date', 'status')
    fieldsets = [
        ("Title", {"fields": ["title"]}),
        ("Description", {"fields": ["description"]}),
        ("Status", {"fields": ["status"]}),
        ("User/Date", {"fields": ["creator", "creation_date"]}),
    ]


admin.site.register(Ticket, TicketAdmin)
