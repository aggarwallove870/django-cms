# Generated by Django 3.2.16 on 2023-01-06 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_alter_flexpage_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signandshareform',
            name='email_address',
        ),
        migrations.RemoveField(
            model_name='signandshareform',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='signandshareform',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='signandshareform',
            name='state',
        ),
    ]
