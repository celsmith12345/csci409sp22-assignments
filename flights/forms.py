from django import forms

# class TicketForm(forms.Form):
    # confirmation_number = forms.IntegerField(label='Confirmation Number')
class FlightForm(forms.Form):
    origin_airport = forms.CharField(label='Origin Airport')
    destination_airport = forms.CharField(label='Destination Airport')