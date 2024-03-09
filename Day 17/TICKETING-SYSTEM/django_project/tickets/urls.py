from django.urls import path
from . import views

urlpatterns = [
    path("ticket-details/<int:pk>/", views.ticket_details, name="ticket_details"),
    path("create-ticket/", views.create_ticket, name="create_ticket"),
    path("update-ticket/<int:pk>/", views.update_ticket, name="update_ticket"),
    path("all-tickets/", views.all_tickets, name="all_tickets"),
    path("ticket-queue/", views.ticket_queue, name="ticket_queue"),
    path("accept-ticket/<int:pk>/", views.accept_ticket, name="accept_ticket"),
    path("close-ticket/<int:pk>/", views.close_ticket, name="close_ticket"),
    path("workspace/", views.workspace, name="workspace"),
    path("all-closed-tickets/", views.all_closed_tickets, name="all_closed_tickets"),
]