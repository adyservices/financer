# Generated by Django 3.2.20 on 2023-09-15 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20230910_1552'),
        ('payments', '0003_rename_bill_paid_to_payments_bill_paid_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='event_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.event'),
        ),
    ]
