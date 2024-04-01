# Generated by Django 5.0.1 on 2024-03-14 07:45

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(db_column='user_id', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(db_column='first_name', max_length=255)),
                ('last_name', models.CharField(db_column='last_name', max_length=255)),
                ('email', models.EmailField(db_column='email', max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at')),
            ],
            options={
                'db_table': 'app_user',
            },
        ),
        migrations.CreateModel(
            name='UserCredential',
            fields=[
                ('user_id', models.OneToOneField(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='five.user')),
                ('username', models.CharField(db_column='username', max_length=255)),
                ('password', models.CharField(db_column='password', max_length=255)),
            ],
            options={
                'db_table': 'app_user_credential',
            },
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
                ('role_name', models.CharField(choices=[('USER', 'User'), ('SURGEON', 'Surgeon'), ('RADIOLOGIST', 'Radiologist'), ('TELERADIOLOGIST', 'Teleradiologist')], db_column='role_name', default='USER', max_length=20)),
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
                ('report_meta', models.JSONField(blank=True, default=dict, null=True)),
                ('org_id', models.ForeignKey(db_column='org_id', on_delete=django.db.models.deletion.CASCADE, to='five.organization')),
                ('uploaded_by', models.ForeignKey(db_column='uploaded_by_id', on_delete=django.db.models.deletion.CASCADE, to='five.user')),
            ],
            options={
                'db_table': 'app_volume_record',
            },
        ),
    ]
