# Generated by Django 4.0.8 on 2022-11-29 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_homepage_nila_intro_carouselitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='nila_intro',
        ),
    ]