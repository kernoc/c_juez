# Generated by Django 3.2.3 on 2021-05-26 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='settled',
            field=models.IntegerField(verbose_name=20),
        ),
    ]
