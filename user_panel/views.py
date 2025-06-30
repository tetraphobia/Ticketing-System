from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login
from .forms import TicketForm, UpdateTicket
from .models import Ticket

# Create your views here.

def register_view(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created succesfully')
            login(request, user)
            return redirect('user')
    else:
        form = UserCreationForm()

    return render(request, 'main/register.html', { "form": form})

def user(request):
    return render(request, 'main/home.html')

def ticket_creation_view(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.creator = request.user
            ticket.save()
            return redirect('user')
    else:
        form = TicketForm()
    return render(request, 'main/ticket_creation.html', {'form': form})

def user_tickets_view(request):
    tickets = Ticket.objects.filter(creator=request.user)
    return render(request, 'main/user_tickets.html', {'tickets': tickets})

def delete_ticket_view(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, creator=request.user)

    if request.method == "POST":
        ticket.delete()
        return redirect('user_tickets')
    
    return render(request, 'main/delete_ticket.html',{'ticket': ticket})

def update_ticket_view(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, creator=request.user)

    if request.method == "POST":
        updated_ticket = UpdateTicket(request.POST, instance=ticket)

        if updated_ticket.is_valid():
            updated_ticket.save()
            return redirect('user_tickets')
    else:
        updated_ticket = UpdateTicket(instance=ticket)
       

    return render(request, 'main/edit_ticket.html', {'form': updated_ticket, 'tickets': ticket})
    


