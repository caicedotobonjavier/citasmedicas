# Generated by Django 5.0.7 on 2024-07-13 17:10

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('tipo_documento', models.CharField(choices=[('0', 'Registro Civil'), ('1', 'Tarjeta Identidad'), ('2', 'Cedula Ciudadania'), ('3', 'Tarjeta Extranjeria'), ('4', 'Otro')], max_length=1, verbose_name='Cedula')),
                ('nro_documento', models.CharField(max_length=20, unique=True, verbose_name='N° Documento')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Correo Electrnico')),
                ('genero', models.CharField(blank=True, choices=[('0', 'Masculino'), ('1', 'Femenino'), ('2', 'Otro')], max_length=1, verbose_name='Genero')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha Nacimiento')),
                ('edad', models.IntegerField(blank=True, verbose_name='Edad')),
                ('telefono', models.CharField(blank=True, max_length=20, verbose_name='Telefono Contacto')),
                ('eps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente_eps', to='eps.eps')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'ordering': ['nombres'],
            },
        ),
    ]
