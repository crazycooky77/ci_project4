# Generated by Django 4.2.1 on 2023-12-23 15:48

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('privacy', models.CharField(choices=[('PRV', 'Private'), ('PUB', 'Public'), ('SH', 'Shared')], default='SH', max_length=20)),
                ('collection_access', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None, null=True), size=None)),
                ('account_type', models.CharField(choices=[('LC', 'Lego Collection'), ('FB', 'Facebook'), ('GGL', 'Google')], max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LegoSet',
            fields=[
                ('set_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('set_name', models.CharField(max_length=200)),
                ('set_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('nr_of_pieces', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LegoCollection',
            fields=[
                ('collection_id', models.AutoField(primary_key=True, serialize=False)),
                ('collection_name', models.CharField(max_length=100)),
                ('missing_pieces', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=None, null=True, size=None)),
                ('build_status', models.CharField(choices=[('NEW', 'New (Owned)'), ('BN', 'Build Next'), ('STORED', 'Stored'), ('WL', 'Wish List')], max_length=50)),
                ('set_location', models.CharField(blank=True, max_length=100, null=True)),
                ('favourited', models.BooleanField()),
                ('shared', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('collection_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lego_collection.legoset')),
            ],
        ),
    ]
