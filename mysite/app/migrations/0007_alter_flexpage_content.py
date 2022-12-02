# Generated by Django 4.0.8 on 2022-11-30 07:04

from django.db import migrations
import streams.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_flexpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Title', required=True)), ('text', wagtail.blocks.TextBlock(help_text='Text', required=True))])), ('richtext', streams.blocks.RichTextBlock()), ('card', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your Title', required=True)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('Image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.blocks.TextBlock(max_length=50, required=True)), ('button', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(required=False))])))])), ('fourdiv', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('Image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.blocks.TextBlock(max_length=50, required=True))])))])), ('footer', wagtail.blocks.StructBlock([('footer', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('Image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.blocks.TextBlock(max_length=50, required=True)), ('ul_title', wagtail.blocks.CharBlock(max_length=40, required=True))])))])), ('Button', wagtail.blocks.StructBlock([('button', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock(max_length=50, required=True)), ('button_url', wagtail.blocks.URLBlock(required=False))])))])), ('leaderboardsection', wagtail.blocks.StructBlock([('leaderboardsection', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('leader_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('leader_name', wagtail.blocks.TextBlock(max_length=300, required=True)), ('leader_university_name', wagtail.blocks.TextBlock(max_length=300, required=True)), ('leader_university_address', wagtail.blocks.TextBlock(max_length=300, required=True))])))])), ('testimonialslider', wagtail.blocks.StructBlock([('testimonialslider', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('caption', wagtail.blocks.TextBlock(max_length=300, required=True)), ('username', wagtail.blocks.TextBlock(max_length=300, required=True)), ('proffesion', wagtail.blocks.TextBlock(max_length=300, required=True))])))])), ('banner', wagtail.blocks.StructBlock([('banner', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('banner_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('banner_overlay_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('banner_overlay_text', wagtail.blocks.TextBlock(max_length=100, required=True)), ('banner_button_1', wagtail.blocks.TextBlock(max_length=100, required=True)), ('banner_button_2', wagtail.blocks.TextBlock(max_length=100, required=True))])))])), ('volunteer', wagtail.blocks.StructBlock([]))], blank=True, null=True, use_json_field=None),
        ),
    ]
