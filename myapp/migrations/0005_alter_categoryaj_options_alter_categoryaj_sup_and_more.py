# Generated by Django 4.2.16 on 2025-04-30 10:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_categoryaj_alter_jobsmodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryaj',
            options={'verbose_name': 'Aniqlangan-jinoyatlar', 'verbose_name_plural': 'Aniqlangan-jinoyatlar'},
        ),
        migrations.AlterField(
            model_name='categoryaj',
            name='sup',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)], verbose_name='bandi'),
        ),
        migrations.AlterField(
            model_name='categoryaj',
            name='title',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)], verbose_name='modda'),
        ),
    ]
