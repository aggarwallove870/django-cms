# Generated by Django 4.0.8 on 2022-11-25 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_navbarlogo'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='icon',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
