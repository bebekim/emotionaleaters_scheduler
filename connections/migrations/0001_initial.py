# Generated by Django 3.0.6 on 2020-06-05 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('core_emotion', models.CharField(choices=[('AFR', 'Afraid'), ('ANG', 'Angry'), ('SHM', 'Ashamed'), ('HPY', 'Happy'), ('HRT', 'Hurt'), ('GTY', 'Guilty'), ('SAD', 'Sad')], default='AFR', max_length=3)),
                ('reason', models.TextField()),
            ],
        ),
    ]
