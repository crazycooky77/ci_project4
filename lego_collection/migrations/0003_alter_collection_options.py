# Generated by Django 4.2.1 on 2024-01-04 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lego_collection', '0002_collection_legoset_legocollection'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['collection_id']},
        ),
    ]