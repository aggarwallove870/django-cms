# Generated by Django 3.2.16 on 2023-01-05 09:17

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0016_fourdivsection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ck_editor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]
