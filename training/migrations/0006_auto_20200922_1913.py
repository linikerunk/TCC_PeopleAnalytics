# Generated by Django 2.2.5 on 2020-09-22 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0005_auto_20200922_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.CharField(blank=True, max_length=10, verbose_name='Data Consulta'),
        ),
    ]