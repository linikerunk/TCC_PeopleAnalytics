# Generated by Django 2.2.5 on 2020-09-16 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='training_type',
        ),
    ]