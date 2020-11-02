from django import forms
from django.forms import ModelForm
from .models import Ticket, TicketHistory, TicketHistory


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['category', 'subcategory', 'final_date',
                  'text', 'awnser', 'file_upload']
        labels = {
            'category': 'Categoria : ',
            'subcategory': 'Subcategoria : ',
            'text': 'Descrição : ',
            'file_upload': 'Anexar arquivos  : '
        }

        widgets = {
            'text': forms.Textarea(
                attrs={'placeholder': 'Caso necessário, informe um telefone e/ou e-mail para retorno do chamado',
                       'rows': 5}),
        }


class TicketUpdateForm(forms.ModelForm):

    file_upload = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True}), required=False, label="Anexar Arquivo : ")

    class Meta:
        model = Ticket
        fields = ['awnser', 'final_date',
                  'file_upload', 'finish']
        labels = {
            'category': 'Categoria : ',
            'subcategory': 'Subcategoria : ',
            'text': 'Descrição : ',
        }