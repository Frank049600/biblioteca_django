# Generated by Django 5.0.4 on 2024-06-18 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0007_alter_acervo_model_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acervo_model',
            name='type_adqui',
        ),
        migrations.AddField(
            model_name='acervo_model',
            name='formato',
            field=models.CharField(choices=[('book', 'Libro'), ('disc', 'Disco')], default='book', max_length=5, verbose_name='formato'),
        ),
        migrations.AlterField(
            model_name='acervo_model',
            name='estado',
            field=models.CharField(choices=[('EXC', 'Excelente'), ('BUE', 'Bueno'), ('REG', 'Regular'), ('MAL', 'Malo')], default='EXC', max_length=3, verbose_name='Estado'),
        ),
    ]