from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse


class IndexHour(TemplateView):
    template_name = 'hour/index.html'