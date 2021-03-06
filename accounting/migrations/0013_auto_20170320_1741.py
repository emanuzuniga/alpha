# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-20 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0012_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrydetail',
            name='date',
            field=models.DateField(null=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='accountlevel',
            name='identifierDigits',
            field=models.PositiveIntegerField(default=1, verbose_name='Digitos de indentificador'),
        ),
        migrations.AlterField(
            model_name='report',
            name='accountsToShow',
            field=models.ManyToManyField(related_name='Show', to='accounting.Account', verbose_name='Cuentas a mostrar'),
        ),
        migrations.AlterField(
            model_name='report',
            name='accountsToSum',
            field=models.ManyToManyField(related_name='Sum', to='accounting.Account', verbose_name='Cuentas a sumar'),
        ),
    ]
