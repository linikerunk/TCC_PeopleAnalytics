""" This is a forms.py that helps to work on the payload of front-end """
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import Employee, CostCenter, Unity


# Sign Up Form
class SignUpForm(UserCreationForm):
    username = forms.CharField(label="Usuário", max_length=50, required=True,
                                help_text="Insira seu usuário.")
    first_name = forms.CharField(label="Primeiro Nome", max_length=30, required=True,
                                help_text='Você deve inserir seu primeiro nome.')
    last_name = forms.CharField(label="Segundo Nome", max_length=30, required=True,
                                help_text='Você deve inserir seu ultimo nome.')
    email = forms.EmailField(label="E-mail", max_length=254, required=True,
                                help_text='Entre com um e-mail válido')

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 
            'email', 'password1', 'password2', ]


    def clean_username(self, *args, **kwargs):
        """Validate that the username if empty or if exists on the database."""
        print("Testando clean_username")
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("Campo Usuário está em branco.")
        elif User.objects.filter(username=username).exists():
            raise forms.ValidationError("Usuário já está cadastrado")
        return username


    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError("E-mail deve ser único.")
    #     return email


    def clean_password1(self, *args, **kwargs):
        pass
    

    def clean_password2(self, *args, **kwargs):
        pass


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
            'andress': 'Endereço',
            'andress_number': 'Número',
            'district': 'Bairro',
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