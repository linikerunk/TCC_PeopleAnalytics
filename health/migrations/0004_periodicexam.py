# Generated by Django 2.2.5 on 2020-10-17 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20201003_0032'),
        ('health', '0003_auto_20200912_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodicExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateField(auto_now_add=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('exame', models.CharField(max_length=150, verbose_name='Exame')),
                ('initial_date', models.CharField(max_length=8, verbose_name='Data inicial')),
                ('final_date', models.CharField(max_length=8, verbose_name='Data inicial')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_exam', to='users.Employee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
