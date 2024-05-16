# Generated by Django 5.0.4 on 2024-05-16 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0004_rename_numeracion_acervo_model_numer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acervo_model',
            name='numer',
        ),
        migrations.AlterField(
            model_name='acervo_model',
            name='colocacion',
            field=models.CharField(max_length=6, verbose_name='Colocación'),
        ),
        migrations.AlterField(
            model_name='acervo_model',
            name='estado',
            field=models.CharField(choices=[('EXC', 'Excelente'), ('BUE', 'Bueno'), ('REG', 'Regular'), ('MAL', 'Malo')], default='EXC', max_length=3, verbose_name='Estado del libro'),
        ),
    ]
