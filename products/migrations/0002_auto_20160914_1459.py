# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-14 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdepartment',
            old_name='productdepartment_code',
            new_name='product_department_code',
        ),
        migrations.RenameField(
            model_name='productdepartment',
            old_name='productdepartment_name',
            new_name='product_department_name',
        ),
        migrations.RenameField(
            model_name='productsubdepartment',
            old_name='productsubdepartment_code',
            new_name='product_subdepartment_code',
        ),
        migrations.RenameField(
            model_name='productsubdepartment',
            old_name='productsubdepartment_department',
            new_name='product_subdepartment_department',
        ),
        migrations.RenameField(
            model_name='productsubdepartment',
            old_name='productsubdepartment_name',
            new_name='product_subdepartment_name',
        ),
        migrations.AddField(
            model_name='product',
            name='product_discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Descuento %'),
        ),
    ]
