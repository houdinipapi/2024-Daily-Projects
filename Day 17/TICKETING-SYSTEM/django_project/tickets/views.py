import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Ticket
from .form import CreateTicketForm, UpdateTicketForm


# Create your views here.

"""For customers"""

# Create a ticket
def create_ticket(request):
    if request.method == "POST":
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.created_by = request.user
            var.ticket_status = "Pending"

            var.save()

            messages.info(request, "Ticket created successfully!")
            return redirect("dashboard")
        else:
            messages.warning(request, "Invalid information!")
            return redirect("create_ticket")
    else:
        form = CreateTicketForm()
        context = {"form": form}

        return render(request, "tickets/create_ticket.html", context)
    