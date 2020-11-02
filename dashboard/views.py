from random import randint
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from utils.decorators import first_register
from chartjs.views.lines import BaseLineChartView
# from .models import


@method_decorator(login_required, name='dispatch')
class IndexDashboard(TemplateView):
    template_name = 'dashboard/index.html'


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
            "Programação para Leigos",
            "Algoritmos e Lógicas deProgramação",
            "Programação em C",
            "Programação em Java",
            "Programação em Python",
            "Banco de Dados"
        ]
        return datasets

    def get_data(self):
        """
        Retorna 6 daatsets para plotar o gráficos

        Cada Linha representa um dataset.
        Cada Coluna representa um label.

        A Quantidade de dados precisa ser igual aos datasets/labels

        12 Label, então 12 colunas.
        6 datasets, então 6 lkinhas
        """

        dados = []
        for l in range(6):
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
