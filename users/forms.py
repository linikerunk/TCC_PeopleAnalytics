""" This is a forms.py that helps to work on the payload of front-end """
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import Employee, CostCenter, Unity


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UnityForm(forms.ModelForm):
    name = forms.CharField(widget=TextInput(
        attrs={'class':'validate', 
        'placeholder': 'Digite o nome da unidade... '}))

    class Meta:
        model = Unity
        fields = "__all__"


class CostCenter(forms.ModelForm):
    number = forms.CharField(widget=TextInput(
        attrs={'class':'validate', 
        'placeholder': 'Digite o número de centro de custo...'}))
        
    class Meta:
        model = CostCenter
        fields = "__all__"

class FuncionarioForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = "__all__"
        
        label = {
            'identifier': 'Chave de identificação : ',
            'name': 'Nome do Funcionário : ',
            'bio': 'Descrição do Funcionário : ',
            'admission': 'Data de Admissão : ',
            'resignation': 'Data de Demissão : ',
            'birth_date': 'Data de Nascimento : ',
            'zip_code': 'CEP : ',
            'email': 'E-mail : ',
            'phone': 'Telefone : ',
            'cpf': 'CPF : ',
            'role': 'Cargo : ',
            'cost_center': 'Centro de Custo : ',
            'gender': 'Gênero : ',
            'photo': 'Foto do Funcionário : ',
            'unity': 'Unidade : ',
            'user': 'Usuário : ',
        }