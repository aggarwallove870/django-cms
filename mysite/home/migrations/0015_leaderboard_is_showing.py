# Generated by Django 4.0.8 on 2022-12-30 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_leaderboard_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaderboard',
            name='is_showing',
            field=models.BooleanField(default=False),
        ),
    ]
