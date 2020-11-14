from random import randint
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from utils.decorators import first_register
from ticket.models import Ticket
from training.models import Event
from chartjs.views.lines import BaseLineChartView, HighchartPlotLineChartView
# from .models import


@login_required
def dashboard(request):
    if request.user.employee.role != "RH":
        return render(request, 'registration/denied_permission.html', {})
    tickets = Ticket.objects.all().order_by('-id')
    number_of_tickets = Ticket.objects.count()
    training = Event.objects.count()
    paginator = Paginator(tickets, 10)
    page = request.GET.get('page', 1)
    obj = paginator.get_page(page)

    return render(request, 'dashboard/index.html', {'tickets': tickets,
    'number_of_tickets': number_of_tickets, 'training': training, 'obj': obj})


class ChangeEmployeeJSONView(BaseLineChartView):

    def get_labels(self):
        """Retorna 12 labels para a repersentação de x """
        labels = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro"
        ]
        return labels

    def get_providers(self):
        """Retorna os nomes dos datasets."""
        datasets = [
            "Colaboradores Noturnos",
            "Colaboradores Matutino",
            "Colaboradores Vespertino"
        ]
        return datasets

    def get_data(self):
        """
        Retorna 6 daatsets para plotar o gráficos

        Cada Linha representa um dataset.
        Cada Coluna representa um label.

        A Quantidade de dados precisa ser igual aos datasets/labels

        12 Label, então 12 colunas.
        6 datasets, então 6 linhas
        """

        dados = []
        for l in range(3):
            for c in range(12):
                dado = [
                    randint(1, 3200), #Jan
                    randint(1, 3200), #Fev
                    randint(1, 3200), #Mar
                    randint(1, 3200), #Abril
                    randint(1, 8200), #Maio
                    randint(1, 7200), #Jun
                    randint(1, 6200), #Jul
                    randint(1, 5200), #Ago
                    randint(1, 2200), #Set
                    randint(1, 10200), #Out
                    randint(1, 8200), #Nov
                    randint(1, 7200), #Dez
                    ]
            dados.append(dado)
        return dados

    def get_dataset_options(self, index, color):
        default_opt = {
            "backgroundColor": "rgba(%d, %d, %d, 0.5)" % color,
            "borderColor": "rgba(%d, %d, %d, 1)" % color,
            "pointBackgroundColor": "rgba(%d, %d, %d, 1)" % color,
            "pointBorderColor": "#451474",
        }
        return default_opt

class GenerateHourJSONView(BaseLineChartView):
    
    def get_labels(self):
        """Retorna 12 labels para a repersentação de x """
        labels = [
            "Outubro",
            "Novembro",
            "Dezembro"
        ]
        return labels

    def get_providers(self):
        """Retorna os nomes dos datasets."""
        datasets = [
            "Horas Extras",
            "Banco de Hora",
            "Horas Negativa"
        ]
        return datasets

    def get_data(self):
        """
        Retorna 6 daatsets para plotar o gráficos

        Cada Linha representa um dataset.
        Cada Coluna representa um label.

        A Quantidade de dados precisa ser igual aos datasets/labels

        12 Label, então 12 colunas.
        6 datasets, então 6 linhas
        """

        dados = []
        for l in range(3):
            for c in range(12):
                dado = [
                    randint(1, 200), #Jan
                    randint(1, 200), #Fev
                    randint(1, 200), #Mar
                    randint(1, 200), #Abril
                    randint(1, 200), #Maio
                    randint(1, 200), #Jun
                    randint(1, 200), #Jul
                    randint(1, 200), #Ago
                    randint(1, 200), #Set
                    randint(1, 200), #Out
                    randint(1, 200), #Nov
                    randint(1, 200), #Dez
                    ]
            dados.append(dado)
        return dados

    def get_dataset_options(self, index, color):
        default_opt = {
            "backgroundColor": "rgba(%d, %d, %d, 0.5)" % color,
            "borderColor": "rgba(%d, %d, %d, 1)" % color,
            "pointBackgroundColor": "rgba(%d, %d, %d, 1)" % color,
            "pointBorderColor": "#fff",
        }
        return default_opt
