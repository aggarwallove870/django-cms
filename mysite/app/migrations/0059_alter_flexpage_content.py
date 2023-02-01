# Generated by Django 4.0.8 on 2023-01-19 12:20

from django.db import migrations
import streams.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0058_alter_flexpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Title', required=True)), ('text', wagtail.blocks.TextBlock(help_text='Text', required=True))])), ('full_richtext', streams.blocks.RichtextBlock()), ('card', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your Title', required=True)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('Image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(required=True)), ('text', wagtail.blocks.TextBlock(required=True)), ('button', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(required=False))])))])), ('fourdiv', wagtail.blocks.StructBlock([])), ('footer', wagtail.blocks.StructBlock([('footer', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('Image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(required=True)), ('text', wagtail.blocks.TextBlock(required=True)), ('ul_title', wagtail.blocks.CharBlock(required=True))])))])), ('Button', wagtail.blocks.StructBlock([('button', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock(required=True)), ('button_url', wagtail.blocks.URLBlock(required=False))])))])), ('leaderboardsection', wagtail.blocks.StructBlock([])), ('testimonialslider', wagtail.blocks.StructBlock([('testimonialslider', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('caption', wagtail.blocks.TextBlock()), ('username', wagtail.blocks.TextBlock()), ('proffesion', wagtail.blocks.TextBlock()), ('rating', wagtail.blocks.TextBlock())])))])), ('banner', wagtail.blocks.StructBlock([('banner', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('banner_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('banner_overlay_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('banner_overlay_text_block1', wagtail.blocks.TextBlock(required=True)), ('banner_overlay_text_block2', wagtail.blocks.TextBlock(required=True)), ('banner_overlay_text_block3', wagtail.blocks.TextBlock(required=True)), ('banner_button_1', wagtail.blocks.TextBlock(required=True)), ('banner_button_url_1', wagtail.blocks.TextBlock(required=True)), ('banner_button_2', wagtail.blocks.TextBlock(required=True)), ('banner_button_url_2', wagtail.blocks.TextBlock(required=True))])))])), ('volunteer', wagtail.blocks.StructBlock([('volunteer', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(required=True)), ('volunteers', wagtail.blocks.TextBlock(required=True)), ('text', wagtail.blocks.TextBlock(required=True))])))])), ('divsection', wagtail.blocks.StructBlock([('divsection', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.TextBlock(required=True)), ('subtitle', wagtail.blocks.TextBlock(required=True)), ('divsection_image', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('studentandeducator', wagtail.blocks.StructBlock([('studenteducator', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('heading_student', wagtail.blocks.TextBlock(required=True)), ('sub_heading_student', wagtail.blocks.TextBlock(required=True)), ('button_text_student', wagtail.blocks.TextBlock(required=True)), ('button_1_url', wagtail.blocks.TextBlock(required=True)), ('heading_educator', wagtail.blocks.TextBlock(required=True)), ('sub_heading_educator', wagtail.blocks.TextBlock(required=True)), ('button_text_educator', wagtail.blocks.TextBlock(required=True)), ('button_2_url', wagtail.blocks.TextBlock(required=True))])))])), ('banner_section_2', wagtail.blocks.StructBlock([('banner_section_2', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('banner_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('banner_overlay_text', wagtail.blocks.TextBlock(required=True))])))])), ('educator_register_form', wagtail.blocks.StructBlock([])), ('student_register_form', wagtail.blocks.StructBlock([])), ('verticalimagewithtext', wagtail.blocks.StructBlock([('vertical', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('Image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('text', wagtail.blocks.TextBlock(required=True))])))])), ('signthispetetionform', wagtail.blocks.StructBlock([])), ('studentachivment', wagtail.blocks.StructBlock([('achivment', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('heading_one', wagtail.blocks.TextBlock(required=True)), ('achivment_scores_one', wagtail.blocks.TextBlock(required=True)), ('heading_two', wagtail.blocks.TextBlock(required=True)), ('achivment_scores_two', wagtail.blocks.TextBlock(required=True)), ('heading_three', wagtail.blocks.TextBlock(required=True)), ('achivment_scores_three', wagtail.blocks.TextBlock(required=True))])))])), ('CustomHtml', wagtail.blocks.StructBlock([('editor', wagtail.blocks.TextBlock(required=True))])), ('LeaderBoardScore', wagtail.blocks.StructBlock([]))], blank=True, null=True, use_json_field=None),
        ),
    ]