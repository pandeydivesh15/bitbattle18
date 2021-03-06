# Generated by Django 2.0 on 2018-08-18 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('email', models.EmailField(max_length=80)),
                ('rating', models.FloatField()),
                ('num_ratings', models.IntegerField()),
            ],
        ),
    ]
