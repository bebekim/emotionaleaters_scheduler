# Generated by Django 3.0.6 on 2020-06-24 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0003_auto_20200616_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
