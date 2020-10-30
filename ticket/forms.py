from django import forms
from django.forms import ModelForm
from .models import Ticket, TicketHistory, TicketHistory


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['text', 'awnser', 'final_date', 'finish',
                  'file_upload', 'employee', 'category', 'subcategory']
