# Generated by Django 3.2.3 on 2021-05-26 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Judicialoffice',
            fields=[
                ('idJudicialoffice', models.AutoField(primary_key=True, serialize=False)),
                ('nameoffice', models.CharField(max_length=150)),
                ('namejudge', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('emaile', models.EmailField(max_length=150)),
                ('country', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.IntegerField(verbose_name=70)),
            ],
        ),
    ]
