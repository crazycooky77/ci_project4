# Generated by Django 4.2.1 on 2023-12-29 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lego_collection', '0003_alter_legocollection_missing_pieces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='privacy',
            field=models.CharField(choices=[('PRV', 'Private'), ('PUB', 'Public'), ('SH', 'Shared')], default='PRV', max_length=20),
        ),
    ]