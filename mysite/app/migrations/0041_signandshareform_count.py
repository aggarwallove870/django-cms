# Generated by Django 3.2.16 on 2023-01-03 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_signandshareform'),
    ]

    operations = [
        migrations.AddField(
            model_name='signandshareform',
            name='count',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]