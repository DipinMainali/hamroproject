# Generated by Django 3.2.5 on 2022-01-27 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0005_remove_places_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
