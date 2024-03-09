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
    

# Updating a ticket
def update_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    form = UpdateTicketForm(instance=ticket)

    if request.method == "POST":
        form = UpdateTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.info(request, "Ticket updated successfully!")
            return redirect("dashboard")
        else:
            messages.warning(request, "Invalid information!")
            # return redirect("update_ticket", pk=pk)
    else:
        form = UpdateTicketForm(instance=ticket)
        context = {"form": form}
        return render(request, "tickets/update_ticket.html", context)
    

# Viewing all created tickets
def all_tickets(request):
    tickets = Ticket.objects.filter(created_by=request.user)
    context = {
        "tickets": tickets
    }

    return render(request, "tickets/all_tickets.html", context)


"""For engineers"""
# View ticket queue

def ticket_queue(request):
    tickets = Ticket.objects.filter(ticket_status="Pending")
    context = {
        "tickets": tickets
    }

    return render(request, "tickets/ticket_queue.html", context)


# Accept a ticket from the queue

def accept_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.assigned_to = request.user
    ticket.ticket_status = "In Progress"
    ticket.accepted_date = datetime.datetime.now()
    ticket.save()

    messages.info(request, "Ticket accepted successfully!")

    return redirect("ticket_queue")


# Close a ticket

def close_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.ticket_status = "Closed"
    ticket.closed_date = datetime.datetime.now()
    ticket.save()

    messages.info(request, "Ticket closed successfully!")

    return redirect("ticket_queue")