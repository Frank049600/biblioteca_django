# Generated by Django 5.0.4 on 2024-04-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proyectos_estadias', '0012_delete_registro'),
    ]

    operations = [
        migrations.CreateModel(
            name='registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'registro',
            },
        ),
    ]
