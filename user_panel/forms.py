from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title', 
            'status',
            'description',
        ]
        
class UpdateTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'status',
            'description',
        ]
Ticket = TicketForm()