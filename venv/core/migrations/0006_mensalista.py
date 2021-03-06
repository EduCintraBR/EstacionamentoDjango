# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-12 12:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_movrotativo_pago'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensalista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField()),
                ('valor_mes', models.DecimalField(decimal_places=2, max_digits=6)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Veiculo')),
            ],
        ),
    ]
