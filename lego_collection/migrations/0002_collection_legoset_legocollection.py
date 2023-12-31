# Generated by Django 4.2.1 on 2024-01-04 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lego_collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('collection_id', models.AutoField(primary_key=True, serialize=False)),
                ('collection_name', models.CharField(max_length=100)),
                ('collection_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('collection_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LegoSet',
            fields=[
                ('set_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('set_name', models.CharField(max_length=200)),
                ('set_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('nr_of_pieces', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['set_number'],
            },
        ),
        migrations.CreateModel(
            name='LegoCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('missing_pieces', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('build_status', models.CharField(choices=[('NEW', 'New (Owned)'), ('BN', 'Build Next'), ('STORED', 'Stored'), ('WL', 'Wish List')], max_length=50)),
                ('set_location', models.CharField(blank=True, max_length=100, null=True)),
                ('favourited', models.BooleanField()),
                ('shared', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('col_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lego_collection.collection')),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lego_collection.legoset')),
            ],
            options={
                'ordering': ['col_id', 'build_status', 'set'],
            },
        ),
    ]
