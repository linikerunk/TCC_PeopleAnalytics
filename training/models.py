from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import Employee


STATE_CHOICES = (('Acre', 'Acre'), ('Alagoas', 'Alagoas'), ('Amapá', 'Amapá'),
                ('Amazonas', 'Amazonas'), ('Bahia', 'Bahia'), ('Ceará', 'Ceará'),
                ('Distrito Federal', 'Distrito Federal'),
                ('Espírito Santo', 'Espírito Santo'), ('Goiás', 'Goiás'), 
                ('Maranhão', 'Maranhão'), ('Mato Grosso', 'Mato Grosso'),
                ('Mato Grosso do Sul', 'Mato Grosso do Sul'), 
                ('Minas Gerais', 'Minas Gerais'), ('Pará', 'Pará'),
                ('Paraíba', 'Paraíba'), ('Paraná', 'Paraná'), 
                ('Pernambuco', 'Pernambuco'), ('Piauí', 'Piauí'), 
                ('Rio de Janeiro', 'Rio de Janeiro'),
                ('Rio Grande do Norte', 'Rio Grande do Norte'), 
                ('Rio Grande do Sul', 'Rio Grande do Sul'), 
                ('Rondônia', 'Rondônia'), ('Roraima', 'Roraima'),
                ('Santa Catarina', 'Santa Catarina'),
                ('São Paulo', 'São Paulo'), ('Sergipe', 'Sergipe'),
                ('Tocantins', 'Tocantins'))

CATEGORY = (('Tecnologia da informação', 'Tecnologia da informação'),
            ('Treinamento online', 'Treinamento online'),
            ('Programas de mentoria', 'Programas de mentoria'),
            ('Coaching empresarial', 'Coaching empresarial'),
            ('Workshops', 'Workshops'),
            ('Gestão do conhecimento', 'Gestão do conhecimento'),
            ('Treinamento presencial com instrutor',
             'Treinamento presencial com instrutor'),
            ('Treinamento de desenvolvimento de Soft Skills',
             'Treinamento de desenvolvimento de Soft Skills'),
            ('Treinamentos obrigatórios', 'Treinamentos obrigatórios'),)



class Training(models.Model):
    training_name = models.CharField('Nome Treinamento', max_length=100)
    category = models.CharField('Categoria', choices=CATEGORY, max_length=50)
    content = models.TextField('Conteúdo')
    required = models.CharField('Requisito', max_length=50)
    resource = models.CharField('Recursos', max_length=50)
    local = models.CharField('Local', max_length=50)
    workload = models.CharField('Carga Horária', max_length=5)

    class Meta:
        verbose_name = "Treinamento"
        verbose_name_plural = "Treinamentos"

    def __str__(self):
        return  ' %s ' % f"{self.training_name}"


class Entity(models.Model):
    entity_name = models.CharField('Nome da Entidade', max_length=100)
    social_reason = models.CharField('Razão Social', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=100)
    contact_person = models.CharField('Pessoa Responsável', max_length=30)
    phone = models.CharField('Telefone', null=True, blank=True, max_length=16)
    zip_code = models.CharField('CEP', max_length=10)
    address = models.CharField('Endereço', max_length=60)
    city = models.CharField('Cidade', max_length=50)
    state = models.CharField('Estado', choices=STATE_CHOICES, max_length=2)
    email = models.EmailField(max_length=70, blank=False, unique=True,
                              verbose_name=u'Email', error_messages={
                              'required': 'Porfavor digite seu e-mail.',
                              'unique': 'Já existe esse e-mail cadastrado.'},)
    
    class Meta:
        verbose_name = "Entidade"
        verbose_name_plural = "Entidades"

    def __str__(self):
        return ' %s ' % f"Nome Entidade : {self.entity_name}"


class Instructor(models.Model):
    register_instructor = models.IntegerField('Registro Instrutor',
                                        primary_key=True, validators=[
                                        MaxValueValidator(9999999999),
                                        MinValueValidator(0000000000)])
    instructor_name = models.CharField('Nome Instrutor', max_length=100)
    instructor_photo = models.ImageField(upload_to='photos_instructor',
                                        null=True, blank=True,
                                        verbose_name=u'Foto do Instrutor')
    training = models.ManyToManyField(Training)

    class Meta:
        verbose_name = "Instrutor"
        verbose_name_plural = "Instrutores"

    def __str__(self):
        return ' %s ' % f"{self.instructor_name}"


class Event(models.Model):
    event_name = models.CharField('Nome do Evento', max_length=80)
    value = models.DecimalField('Valor', max_digits=8, decimal_places=2,
                                default=0)
    event_date = models.CharField('Data Consulta', max_length=10, blank=True)
    present_list = models.FileField('Lista de Presença',
                                upload_to="present_list", default="", null=True,
                                blank=True)
    training = models.ForeignKey(Training, related_name="event", default="",
                                blank=True, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, related_name="event", default="",
                                blank=True, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, related_name="event", default="",
                                blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return  ' %s ' % f"{self.event_name}"