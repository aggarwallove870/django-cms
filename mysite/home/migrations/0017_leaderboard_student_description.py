# Generated by Django 3.2.16 on 2023-01-09 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20230109_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaderboard',
            name='student_description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]