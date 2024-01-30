# Generated by Django 4.2.1 on 2024-01-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lego_collection', '0010_alter_legocollection_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legocollection',
            name='build_status',
            field=models.CharField(choices=[('NEW', 'New (Owned)'), ('BN', 'Build Next'), ('B', 'Built'), ('STORED', 'Stored'), ('WL', 'Wish List')], max_length=50),
        ),
    ]
