# Generated by Django 3.2.11 on 2022-01-22 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20220122_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendeduser',
            name='preference',
        ),
        migrations.DeleteModel(
            name='preferences',
        ),
    ]
