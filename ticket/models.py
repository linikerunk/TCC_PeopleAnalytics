import os
from datetime import datetime
from django.db import models
from django.utils import timezone
from model_utils.models import TimeStampedModel
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import Employee
from django.conf import settings

BOOL_CHOICES = ((True, 'Sim'), (False, 'Não'))


class SubCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    subcategory = models.ManyToManyField(SubCategory)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    text = models.TextField(blank=False, verbose_name="Descrição")
    awnser = models.TextField(
        blank=True, null=True, verbose_name="Resposta :")
    date = models.DateTimeField(auto_now_add=True)
    final_date = models.DateTimeField(
        null=True, blank=True, verbose_name="Data Finalizada : ")
    finish = models.BooleanField(default=False, choices=BOOL_CHOICES)
    file_upload = models.FileField(
        blank=True, upload_to='tickets', verbose_name="Anexar Arquivos : ")
    employee = models.ForeignKey(
        Employee, related_name="tickets", on_delete=models.PROTECT)
    category = models.ForeignKey(
        Category, related_name='tickets', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(
        SubCategory, related_name='tickets', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.finish:
            if not self.final_date:
                pass
                self.final_date = timezone.now()
        return super(Ticket, self).save(*args, **kwargs)

    def open_time(self):
        time = timezone.now() - self.date
        time = time.days
        if time == 0:  # Ajuste no tempo
            time = 1
        print(time)
        return time

    def finish_time(self):
        print(self.finish_time)
        if self.finish_time:
            finish_time = self.finish_time - self.date
            if abs(finish_time.days) == 0:
                finish_time = 1
                return abs(finish_time)
            return abs(finish_time.days)
        return 1

    def __str__(self):
        return f'Ticket Número {self.pk}, Funcionário {self.employee.identifier}'


class TicketHistory(models.Model):
    date_message = models.DateTimeField()
    message = models.TextField(
        blank=True, null=True, verbose_name="Mensagem :")
    ticket = models.ForeignKey(
        Ticket, related_name='historico', on_delete=models.CASCADE)
    employee = models.ForeignKey(
        Employee, related_name="historico", on_delete=models.PROTECT)

    def __str__(self):
        return f'Mensagem de {self.employee} referênte ao Ticket {self.ticket.pk}, data :{self.date_message}'