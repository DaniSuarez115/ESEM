# Generated by Django 4.2.4 on 2024-09-24 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
    ]
