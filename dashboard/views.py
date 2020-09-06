from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from utils.decorators import first_register
# from .models import


@method_decorator(login_required, name='dispatch')
class IndexDashboard(TemplateView):
    template_name = 'dashboard/index.html'