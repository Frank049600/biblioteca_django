# Generated by Django 5.0.4 on 2024-04-25 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos_estadias', '0008_rename_proyectos_proyecto_alter_proyecto_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='proyecto',
        ),
    ]