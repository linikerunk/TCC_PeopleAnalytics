# Generated by Django 2.2.5 on 2020-11-01 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='employee',
            new_name='employee_t',
        ),
    ]