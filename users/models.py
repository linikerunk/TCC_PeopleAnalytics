from django.conf import settings
from datetime import datetime   
from django.db import models
from django.contrib.auth.models import User, Group
from stdimage import StdImageField, JPEGField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


PHOTOS_FOLDER = "FotosFuncionarios/"
DEFAULT = '0000.jpg'
GENDER_CHOICES = (
        ('Feminino', 'Feminino'),
        ('Masculino', 'Masculino'),
        ('N/A', 'N/A'),)
LOCOMOTION = (
        ('Carro', 'Carro'),
        ('Moto', 'Moto'),
        ('Transporte Publico', 'Transporte publico'),
        ('Caminhada a pé', 'Caminhada a pé'),)
current_date = datetime.now()


class Base(models.Model):
    created = models.DateField('Criação', auto_now_add=True)
    modified = models.DateField('Atualização', auto_now_add=True)
    active = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Unity(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name = "Unidade"
        verbose_name_plural = "Unidades"

    def __str__(self):
        return self.name


class CostCenter(models.Model):
    number = models.CharField('Centro de Custo', primary_key=True,
                              max_length=50, blank=False)
    name_department = models.CharField('Departamento', max_length=60)
    responsible = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Centro de Custo"
        verbose_name_plural = "Centro de Custos"

    def __str__(self):
        return  self.number


# class Andress(Base):
#     zip_code = models.CharField('CEP', max_length=10, blank=True)
#     andress = models.CharField("Endereço", max_length=200, blank=True)
#     andress_number = models.CharField("Número", max_length=6, blank=True)

#     def __str__(self):
#         return self.zip_code


class Employee(models.Model):
    identifier = models.AutoField(auto_created = True, primary_key = True,
                                  serialize = False,  verbose_name ='ID')
    name = models.CharField("Nome Funcionário", max_length=130, null=False)
    bio = models.TextField("Bio", max_length=200, blank=True)
    admission = models.DateTimeField("Admissão", blank=True)
    resignation = models.DateTimeField("Demissão", null=True, blank=True)
    birth_date = models.DateTimeField("Data de Aniversário", null=True,
                                    blank=True)
    zip_code = models.CharField('CEP', max_length=10, blank=True)
    andress = models.CharField("Endereço", max_length=200, blank=True)
    andress_number = models.CharField("Número", max_length=6, blank=True)
    district = models.CharField("Bairro", max_length=100, blank=True)
    email = models.EmailField('Email', max_length=70, blank=True, null=True,
                                    error_messages={
                                    'required': 'Porfavor digite seu e-mail.',
                                'unique': 'Já existe esse e-mail cadastrado.'})
    phone = models.CharField('Telefone', max_length=15, null=True)
    cpf = models.CharField('CPF', max_length=11, blank=False)
    role = models.CharField('Cargo', max_length=60, blank=False)
    locomotion = models.CharField('Locomoção', max_length=60, choices=LOCOMOTION)
    cost_center = models.ForeignKey(CostCenter, null=True, 
                                    verbose_name="Centro de Custo",
                                    on_delete=models.PROTECT)
    gender = models.CharField('Gênero', max_length=12, choices=GENDER_CHOICES)
    photo = StdImageField(upload_to='FotosFuncionarios', default=DEFAULT,
                                    variations={'thumbnail': 
                                    {'width': 100, 'height': 75}})
    unity = models.ForeignKey(Unity, related_name="funcionarios", null=True,
                                    on_delete=models.PROTECT)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True,
                                    related_name="employee",
                                    null=True, on_delete=models.CASCADE)

    def get_photo_url(self):
        path = f'{PHOTOS_FOLDER}/{self.identifier}.JPG'

        if default_storage.exists(path):
            return default_storage.open(path).name

        return default_storage.open(f'{PHOTOS_FOLDER}/{DEFAULT}').name

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"


    def save(self, *args, **kwargs):
        self.admission = current_date
        print(f"data da admissao : {self.admission}")
        return super().save(*args, **kwargs)


    def __str__(self):
        return  self.name


# @receiver(post_save, sender=User)
# def create_user_employee(sender, instance, created, **kwargs):
#     if created:
#         query = Employee.objects.filter(identifier=instance.id)
#         if query :
#             return 0
#         employee = Employee.objects.create(identifier=instance.id,
#             name=(instance.first_name + " " + instance.last_name),
#             user=instance, admission=current_date)
#         employee.save()
        