
from django.db import models
from datetime import datetime  
from django.utils import timezone 
from users.models import Employee

# Create your models here.
current_date = datetime.now()

class AbsenteeismRate(models.Model):
    employee = models.ForeignKey(Employee, related_name='rate_abis' , null=True, 
            verbose_name="Funcionário",  on_delete=models.PROTECT)
    absenteeism_days = models.IntegerField("Dias de absenteismo")
    days_month = models.IntegerField("Dias no mês")
    date_register = models.DateTimeField("Mês referente ao calculo",
                                        default=timezone.now)
    absenteeism = models.DecimalField("Absenteísmo", max_digits=5,
                                        decimal_places=2, blank=True)
    
    def save(self, *args, **kwargs): 
        self.absenteeism =  (((self.absenteeism_days / self.days_month) * 100) / 100) * 100
        super(AbsenteeismRate, self).save(*args, **kwargs) 

    def __str__(self):
        return f'{self.absenteeism}'