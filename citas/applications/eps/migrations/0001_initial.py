# Generated by Django 5.0.7 on 2024-07-13 16:40

import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('nombre', models.CharField(max_length=50, verbose_name='Eps')),
            ],
            options={
                'verbose_name': 'EPS',
                'verbose_name_plural': 'EPS',
                'ordering': ['nombre'],
            },
        ),
    ]
