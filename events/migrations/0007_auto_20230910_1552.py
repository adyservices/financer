# Generated by Django 3.2.20 on 2023-09-10 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20230910_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_pic',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.TextField(),
        ),
    ]
