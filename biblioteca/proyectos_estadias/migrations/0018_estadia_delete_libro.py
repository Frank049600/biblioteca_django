# Generated by Django 5.0.4 on 2024-04-25 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos_estadias', '0017_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estadia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Estadia',
                'verbose_name_plural': 'Estadias',
            },
        ),
        migrations.DeleteModel(
            name='Libro',
        ),
    ]