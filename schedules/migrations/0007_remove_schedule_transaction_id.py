# Generated by Django 3.0.6 on 2020-07-04 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0006_schedule_acts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='transaction_id',
        ),
    ]
