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
from chartjs.views.lines import BaseLineChartView, HighchartPlotLineChartView
# from .models import


@method_decorator(login_required, name='dispatch')
class IndexDashboardView(ListView):
    model = Ticket
    template_name = 'dashboard/index.html'
    queryset = Ticket.objects.all()
    context_object_name = 'obj'
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super(IndexDashboardView, self).get_context_data(**kwargs)
        obj = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(employee , self.paginate_by)
        try:
            obj = paginator.page(page)
        except PageNotAnInteger:
            obj = paginator.page(1)
        except EmptyPage:
            obj  = paginator.page(paginator.num_pages)
        context['obj'] = obj
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = Ticket.objects.all()
        return context


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
