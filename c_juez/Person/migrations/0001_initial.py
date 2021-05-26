# Generated by Django 3.2.3 on 2021-05-26 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('idPerson', models.AutoField(primary_key=True, serialize=False)),
                ('identificationnumber', models.IntegerField(max_length=12)),
                ('idtype', models.CharField(max_length=3)),
                ('gender', models.CharField(max_length=3)),
                ('name1', models.CharField(max_length=30)),
                ('name2', models.CharField(max_length=30)),
                ('surname1', models.CharField(max_length=30)),
                ('surname2', models.CharField(max_length=30)),
                ('residenceaddress', models.CharField(max_length=150)),
                ('emaile', models.EmailField(max_length=150)),
                ('countryorigin', models.CharField(max_length=70)),
                ('cityorigin', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=70)),
            ],
        ),
    ]