# Generated by Django 4.0.8 on 2022-12-01 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0014_contactpage_formfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formfield',
            name='page',
        ),
        migrations.DeleteModel(
            name='ContactPage',
        ),
        migrations.DeleteModel(
            name='FormField',
        ),
    ]
