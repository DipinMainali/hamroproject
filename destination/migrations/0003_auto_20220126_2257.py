# Generated by Django 3.2.11 on 2022-01-26 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0002_auto_20220126_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='places',
            name='thumbnail_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]