# Generated by Django 3.2.16 on 2023-01-03 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_alter_flexpage_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signandshareform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email_address', models.EmailField(max_length=244)),
                ('state', models.CharField(max_length=255)),
            ],
        ),
    ]
