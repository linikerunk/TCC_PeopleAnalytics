from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from datetime import time
from django.utils.timezone import now
from users.models import Employee, Base


CLASSIFICATION = (("Verde", "Verde"), ("Amarelo", "Amarelo"),
                  ("Vermelho", "Vermelho"), ("Azul", "Azul"),)
IMC = (("Magreza grave", "Magreza grave"), 
        ("Magreza moderada", "Magreza moderada"),
        ("Magreza leve", "Magreza leve"), ("Saudável", "Saudável"),
        ("Sobrepeso", "Sobrepeso"), ("Obesidade Grau I", "Obesidade Grau I"),
        ("Obesidade Grau II (severa)", "Obesidade Grau II (severa)"),
        ("Obesidade Grau III (mórbida)", "Obesidade Grau III (mórbida)"),)


class BodyMassIndex(Base):
    identifier = models.ForeignKey(Employee, unique=False,
                                    related_name="employee",
                                    on_delete=models.PROTECT)
    weighing_date = models.DateTimeField("Data Pesagem", default=datetime.now,
                                         editable=False)
    weight = models.DecimalField("Peso", max_digits=5, decimal_places=2)
    height = models.DecimalField("Altura", max_digits=5, decimal_places=2)
    abdominal_circumference = models.DecimalField(
                                    "Circunferência Abdominal(cm)",
                                    max_digits=5, decimal_places=2)
    systolic_blood_pressure = models.DecimalField("Pressão Arterial Sistólica",
                                    max_digits=5, decimal_places=2)
    diastolic_blood_pressure = models.DecimalField(
                                    "Pressão Arterial Diastólica",
                                    max_digits=5, decimal_places=2)   
    classification =  models.CharField("Classificação", max_length=8,
                                    choices=CLASSIFICATION, blank=True)
    classification_text =  models.CharField("Classificação IMC", max_length=28,
                                    choices=IMC, blank=True)
    imc = models.DecimalField("IMC", max_digits=5, decimal_places=2, blank=True)

    class Meta:
        verbose_name = "Indice de Massa Corporal"
        verbose_name_plural = "Indice de Massa Corporal"

    def __str__(self):
        return self.identifier.name

    def save(self, *args, **kwargs):
        self.imc = (self.weight / self.height**2)
        if self.imc < 16:
            self.classification_text = "Magreza grave"
        elif self.imc < 17:
            self.classification_text = "Magreza moderada"
        elif self.imc < 18.5:
            self.classification_text = "Magreza leve"
        elif self.imc < 25:
            self.classification_text = "Saudável"
        elif self.imc < 30:
            self.classification_text = "Sobrepeso"
        elif self.imc < 35:
            self.classification_text = "Obesidade Grau I"
        elif self.imc < 40:
            self.classification_text = "Obesidade Grau II (severa)"
        elif self.imc > 40:
            self.classification_text = "Obesidade Grau III (mórbida)"

        if self.systolic_blood_pressure <= 120 and self.diastolic_blood_pressure <= 80:
            self.classification = "Verde"
        elif self.systolic_blood_pressure <= 120 and self.diastolic_blood_pressure > 80:
            self.classification = "Azul"
        elif self.systolic_blood_pressure <= 139 and self.diastolic_blood_pressure <= 89:
            self.classification = "Azul"
        elif self.systolic_blood_pressure <= 139 and self.diastolic_blood_pressure > 89:
            self.classification = "Amarelo"
        elif self.systolic_blood_pressure <= 159 and self.diastolic_blood_pressure <= 99:
            self.classification = "Amarelo"
        elif self.systolic_blood_pressure <= 159 and self.diastolic_blood_pressure > 99:
            self.classification = "Vermelho"
        elif self.systolic_blood_pressure >= 160 and self.diastolic_blood_pressure >= 100:
            self.classification = "Vermelho"
        return super().save(*args, **kwargs) 
    