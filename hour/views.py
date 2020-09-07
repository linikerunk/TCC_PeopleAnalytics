from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
import requests


class IndexHour(TemplateView):
    # model = 
    template_name = 'hour/index.html'

    def get(self, request, *args, **kwargs):
        nome_cidade = request.POST.get('cidade')
        tempo = requests.get(f"https://api.hgbrasil.com/weather?key=32e5ba65&city_name={nome_cidade}")
        print("Dados Tempo : ", tempo.json())
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)