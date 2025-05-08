from django.contrib import admin
from .models import Ticket, ResponseTicket

admin.site.register(Ticket)
admin.site.register(ResponseTicket)