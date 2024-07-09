# Generated by Django 5.0.6 on 2024-07-09 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0013_alter_acervo_model_anio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acervo_model',
            old_name='fechaRegistro',
            new_name='fecha_registro',
        ),
        migrations.AddField(
            model_name='acervo_model',
            name='fecha_edicion',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de actualización'),
        ),
    ]