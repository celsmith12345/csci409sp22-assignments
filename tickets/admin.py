from django.contrib import admin
from .models import Reservation, Ticket

# Register your models here.
class TicketInLine(admin.StackedInline):
    model = Ticket  # Specify which model to use
    extra = 2  # How many to start with

class ReservationAdmin(admin.ModelAdmin):
    fields = [
        'flight', 'num_people', 'total_cost'
    ]
    inlines = [TicketInLine]  # Load the RunwayInLine Class

admin.site.register(Reservation, ReservationAdmin)
# Register your models here.
