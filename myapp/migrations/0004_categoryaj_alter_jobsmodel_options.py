# Generated by Django 4.2.16 on 2025-04-30 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_jobsmodel_alter_usermodelinfo_tashkilot_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryAJ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.IntegerField(max_length=3, verbose_name='modda')),
                ('sup', models.IntegerField(blank=True, max_length=3, null=True, verbose_name='bandi')),
            ],
        ),
        migrations.AlterModelOptions(
            name='jobsmodel',
            options={'verbose_name': 'Kasb', 'verbose_name_plural': 'Kasblar'},
        ),
    ]
