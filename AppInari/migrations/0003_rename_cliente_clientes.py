# Generated by Django 4.2.4 on 2023-09-12 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppInari', '0002_remove_cliente_direccion_cliente_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cliente',
            new_name='Clientes',
        ),
    ]
