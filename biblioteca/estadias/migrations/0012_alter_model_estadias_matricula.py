# Generated by Django 5.0.6 on 2024-08-12 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadias', '0011_model_estadias_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_estadias',
            name='matricula',
            field=models.IntegerField(),
        ),
    ]