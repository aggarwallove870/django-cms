# Generated by Django 4.0.8 on 2022-12-22 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_carouselitem_proffesion_carouselitem_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='leaderboard',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]