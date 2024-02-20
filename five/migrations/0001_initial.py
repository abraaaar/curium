# Generated by Django 5.0.1 on 2024-02-20 06:00

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_id', models.UUIDField(db_column='user_id', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='%(app_label)s_%(class)s_related', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='%(app_label)s_%(class)s_related', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'app_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('org_id', models.UUIDField(db_column='org_id', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('org_name', models.CharField(db_column='org_name', max_length=255)),
                ('org_description', models.TextField(db_column='org_description')),
                ('org_address', models.TextField(db_column='org_address')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at')),
                ('org_owner', models.ForeignKey(db_column='org_owner_id', on_delete=django.db.models.deletion.CASCADE, to='five.user')),
            ],
            options={
                'db_table': 'app_organization',
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('membership_id', models.UUIDField(db_column='membership_id', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role_name', models.CharField(choices=[('ADMIN', 'Admin'), ('SURGEON', 'Surgeon'), ('TELERADIOLOGIST', 'Teleradiologist')], db_column='role_name', default='ADMIN', max_length=20)),
                ('org_id', models.ForeignKey(db_column='org_id', on_delete=django.db.models.deletion.CASCADE, to='five.organization')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='five.user')),
            ],
            options={
                'db_table': 'app_membership',
            },
        ),
        migrations.CreateModel(
            name='VolumeRecord',
            fields=[
                ('record_id', models.UUIDField(db_column='record_id', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('upload_date', models.DateTimeField(auto_now_add=True, db_column='upload_date')),
                ('status', models.CharField(choices=[('UPLOADED', 'Uploaded'), ('QUEUED', 'Queued'), ('PROCESSING', 'Processing'), ('INTERMEDIATE_STATE', 'Intermediate State'), ('COMPLETED', 'Completed')], db_column='status', default='UPLOADED', max_length=20)),
                ('patient_id', models.CharField(db_column='patient_id', max_length=255)),
                ('study_id', models.CharField(db_column='study_id', max_length=255)),
                ('isAutomated', models.BooleanField(db_column='is_automated', default=False)),
                ('volume_meta', models.JSONField(blank=True, null=True)),
                ('org_id', models.ForeignKey(db_column='org_id', on_delete=django.db.models.deletion.CASCADE, to='five.organization')),
                ('uploaded_by', models.ForeignKey(db_column='uploaded_by_id', on_delete=django.db.models.deletion.CASCADE, to='five.user')),
            ],
            options={
                'db_table': 'app_volume_record',
            },
        ),
    ]
