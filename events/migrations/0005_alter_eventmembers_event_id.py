# Generated by Django 3.2.20 on 2023-09-08 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_rename_customuser_id_eventmembers_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmembers',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_members', to='events.event'),
        ),
    ]
