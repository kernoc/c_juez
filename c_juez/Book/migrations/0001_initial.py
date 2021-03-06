# Generated by Django 3.2.3 on 2021-05-26 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('idBook', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('datei', models.DateField()),
                ('settled', models.IntegerField(max_length=20)),
                ('input', models.FloatField()),
                ('output', models.FloatField()),
                ('balancebook', models.FloatField()),
                ('observations', models.CharField(max_length=50)),
            ],
        ),
    ]
