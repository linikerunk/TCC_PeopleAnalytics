# Generated by Django 2.2.5 on 2020-11-13 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hour', '0005_auto_20201113_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absenteeismrate',
            name='absenteeism',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Absenteeism'),
        ),
    ]
