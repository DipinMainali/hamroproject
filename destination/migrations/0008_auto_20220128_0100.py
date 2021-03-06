# Generated by Django 3.2.11 on 2022-01-27 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0007_auto_20220128_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destimagesfile',
            name='image_file',
            field=models.ImageField(upload_to='destimages'),
        ),
        migrations.AlterField(
            model_name='destimagesfile',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destination.places'),
        ),
    ]
