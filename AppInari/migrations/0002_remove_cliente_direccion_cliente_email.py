# Generated by Django 4.2.4 on 2023-09-12 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppInari', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='direccion',
        ),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]