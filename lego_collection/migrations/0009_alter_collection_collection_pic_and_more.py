# Generated by Django 4.2.1 on 2024-01-09 13:27

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lego_collection', '0008_alter_collection_collection_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='collection_pic',
            field=cloudinary.models.CloudinaryField(default='col-placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='legoset',
            name='set_picture',
            field=cloudinary.models.CloudinaryField(default='set-placeholder', max_length=255, verbose_name='image'),
        ),
    ]
