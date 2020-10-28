from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.tokens import default_token_generator    
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import View, TemplateView, ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from utils.decorators import FirstRegisterMixin

from .forms import SignUpForm
from .tokens import account_activation_token
from .models import Employee, Unity, CostCenter

UserModel = get_user_model()

""" All classes that references a Users """
@method_decorator(login_required, name='dispatch')
class EmployeeListView(ListView):
    model = Employee
    template_name = 'users/index.html'
    queryset = Employee.objects.all()
    context_object_name = 'employee'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        employee = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(employee , self.paginate_by)
        try:
            employee = paginator.page(page)
        except PageNotAnInteger:
            employee = paginator.page(1)
        except EmptyPage:
            employee  = paginator.page(paginator.num_pages)
        context['employee'] = employee
        print(self.request.user.employee) 
        return context


@method_decorator(login_required, name='dispatch')
class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'users/user_create.html'
    fields = '__all__'
    success_url = reverse_lazy('users:users_list')

    def get_context_data(self, **kwargs):
        context = super(EmployeeCreateView, self).get_context_data(**kwargs)
        context['unity'] = Unity.objects.all()
        context['cost_center'] = CostCenter.objects.all()
        context['user'] = User.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        form = super(EmployeeCreateView, self).get_form()
        context = {'form': form}
        initial_base = self.get_initial()
        form.initial = initial_base
        context['unity'] = Unity.objects.all()
        context['cost_center'] = CostCenter.objects.all()
        context['user'] = User.objects.all()
        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        # Verify form is valid
        if form.is_valid():
            # Call parent form_valid to create model record object
            super(EmployeeCreateView,self).form_valid(form)
            # Add custom success message
            messages.success(request, 'Funcionário foi registrado com sucesso.')    
            # Redirect to success page    
            return HttpResponseRedirect(self.get_success_url())
       
        # form['cpf'].value() = filter(lambda parameter_list: expression)
        # Form is invalid
        # Set object to None, since class-based view expects model record object
        self.object = None
        # Return class-based view form_invalid to generate form with errors
        return self.form_invalid(form)



@method_decorator(login_required, name='dispatch')
class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'users/user_update.html'
    fields = '__all__'
    slug_field = 'employee_slug'
    success_url = reverse_lazy('users:users_list')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)
    

@method_decorator(login_required, name='dispatch')
class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'users/user_delete.html'
    success_url = reverse_lazy('users:users_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, f'Funcionário {self.object.name} foi desligado com sucesso.') 
        return HttpResponseRedirect(self.success_url)


class FirstRegisterView(View):
    def get(self, request):
        return render(request, 'registration/register.html', {})


# Login and Logout..
class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('dashboard:dashboard'))
            
        return render(request, 'registration/login.html', { 'form':  AuthenticationForm })

    # really low level
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user is None:
                return render(
                    request,
                    'registration/login.html',
                    { 'form': form, 'invalid_creds': True }
                )

            try:
                form.confirm_login_allowed(user)
            except ValueError:
                return render(
                    request,
                    'registration/login.html',
                    { 'form': form, 'invalid_creds': True }
                )
            login(request, user)

            return redirect(reverse('dashboard:dashboard'))
        else:
            messages.error(request, ('Usuário ou Senha inválidos, \
            verifique novamente o seu login.'))

            return render(request, 'registration/login.html',
                                     { 'form':  AuthenticationForm,})


# Sign Up View
class SignUpView(View):
    form_class = SignUpForm
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = False # Deactivate account till it is confirmed
            user.save()

            current_site = get_current_site(request)
            subject = '🔑 Ative sua conta no Enginee RH'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            messages.success(request, (' \
            Porfavor confirme seu e-mail para completar o registro.'))

            return redirect('users:login')

        return render(request, self.template_name, {'form': form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        return render(request, 'registration/acc_active_email.html')
    else:
        return render(request, 'registration/acc_active_email.html')


@login_required
def my_logout(request):
    logout(request)
    return redirect('users:login')


class ActivateAccount(View):

   def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.email = True
            user.save()
            login(request, user)
            messages.success(request, ('Sua conta foi confirmada.'))
            return redirect('dashboard:dashboard')
        else:
            messages.warning(request, ('A link de confirmação está inválido, \
                possivelmente esse token já está sendo usado.'))
            return redirect('dashboard:dashboard')
