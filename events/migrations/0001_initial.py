# Generated by Django 3.2.20 on 2023-09-04 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('event_description', models.TextField(max_length=100)),
                ('event_pic', models.CharField(max_length=200)),
                ('event_start_date', models.DateField()),
                ('event_end_date', models.DateField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=500)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('ADMIN', 'ADMIN'), ('MANAGER', 'MANAGER'), ('VOLUNTEER', 'VOLUNTEER')], max_length=10)),
                ('added_through', models.CharField(choices=[('ADMIN', 'ADMIN'), ('MANAGER', 'MANAGER'), ('INVITED', 'INVITED')], max_length=10)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('CustomUser_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_members_added_by', to=settings.AUTH_USER_MODEL)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
        migrations.CreateModel(
            name='Activites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('activity_at', models.DateTimeField()),
                ('status', models.CharField(choices=[('ON_GOING', 'ON_GOING'), ('UP_COMING', 'UP_COMING'), ('COMPLETED', 'COMPLETED')], max_length=10)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
    ]
