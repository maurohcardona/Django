# Generated by Django 5.0.2 on 2024-02-24 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0002_alter_clients_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='address',
            field=models.CharField(max_length=50, verbose_name='The address'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='tel',
            field=models.CharField(max_length=10, verbose_name='Telephone'),
        ),
    ]
