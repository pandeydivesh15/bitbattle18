# Generated by Django 2.0 on 2018-08-21 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_pastsearch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pastsearch',
            old_name='loaction_lat',
            new_name='location_lat',
        ),
    ]
