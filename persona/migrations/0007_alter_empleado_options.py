# Generated by Django 4.0.4 on 2022-06-24 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0006_empleado_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['first_name', 'last_name'], 'verbose_name': 'El Empleado', 'verbose_name_plural': 'Empleados de la empresa'},
        ),
    ]
