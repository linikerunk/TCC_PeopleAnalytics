from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, TemplateView, ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import User, Unity, CostCenter

""" All classes that references a Users """
@method_decorator(login_required, name='dispatch')
class UsersListView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'user'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        user = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(user, self.paginate_by)
        try:
            user = paginator.page(page)
        except PageNotAnInteger:
            user = paginator.page(1)
        except EmptyPage:
            user = paginator.page(paginator.num_pages)
        context['user'] = user
        return context


@method_decorator(login_required, name='dispatch')
class UsersCreateView(CreateView):
    model = User
    template_name = 'users/user_create.html'
    fields = '__all__'
    success_url = reverse_lazy('users_list')


@method_decorator(login_required, name='dispatch')
class UsersUpdateView(UpdateView):
    model = User
    template_name = 'users/user_update.html'
    fields = '__all__'
    success_url = reverse_lazy('users_list')


@method_decorator(login_required, name='dispatch')
class UsersDeleteView(DeleteView):
    model = User
    template_name = 'users/user_delete.html'
    success_url = reverse_lazy('users-list')


# Login and Logout..
def login(request):
    context = {}
    return render(request, 'login.html', context)

    
@login_required
def my_logout(request):
    logout(request)
    return redirect('login')

