# Generated by Django 2.2.5 on 2020-10-30 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0011_auto_20201024_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Descrição')),
                ('awnser', models.TextField(blank=True, null=True, verbose_name='Resposta :')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('final_date', models.DateTimeField(blank=True, null=True, verbose_name='Data Finalizada : ')),
                ('finish', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=False)),
                ('file_upload', models.FileField(blank=True, upload_to='tickets', verbose_name='Anexar Arquivos : ')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='ticket.Category')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tickets', to='users.Employee')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='ticket.SubCategory')),
            ],
        ),
        migrations.CreateModel(
            name='TicketHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_message', models.DateTimeField()),
                ('message', models.TextField(blank=True, null=True, verbose_name='Mensagem :')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='historico', to='users.Employee')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historico', to='ticket.Ticket')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='subcategory',
            field=models.ManyToManyField(to='ticket.SubCategory'),
        ),
    ]
