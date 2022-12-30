# Generated by Django 4.0.8 on 2022-12-29 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('app', '0035_alter_flexpage_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('menu_order', models.IntegerField(default=0, help_text='Setup custom menu order')),
            ],
            options={
                'verbose_name': 'Services',
                'verbose_name_plural': 'Services',
            },
            bases=('wagtailcore.page',),
        ),
    ]
