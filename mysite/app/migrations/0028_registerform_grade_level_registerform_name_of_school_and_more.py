# Generated by Django 4.0.8 on 2022-12-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_remove_registerform_grade_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerform',
            name='grade_level',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registerform',
            name='name_of_school',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registerform',
            name='state',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
