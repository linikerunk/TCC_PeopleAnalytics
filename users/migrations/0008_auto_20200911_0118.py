# Generated by Django 2.2.5 on 2020-09-11 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200911_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='admission',
            field=models.DateTimeField(blank=True, verbose_name='Admissão'),
        ),
    ]
