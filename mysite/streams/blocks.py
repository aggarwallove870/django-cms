from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import PageChooserBlock ,StreamBlock, StructBlock
from wagtail.images.apps import WagtailImagesAppConfig
from wagtail.core.blocks import RawHTMLBlock
from ckeditor.fields import RichTextField
from menu.models import Ck_editor
from django import forms
from wagtail.core.templatetags.wagtailcore_tags import richtext




class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""

    def get_api_representation(self, value, context=None):
        return richtext(value.source)

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Richtext without (limited) all the features."""

    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs
    ):  # noqa
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link"]

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"


class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True,help_text="Title")
    text = blocks.TextBlock(required=True,help_text="Text")
    class Meta:
        template ="streams/title_and_text.html"
        icon="edit"
        label= "Title and Text"


class RichTextBlock(blocks.StructBlock):
    caption = blocks.RichTextBlock(
    required=False,
    label='Caption',
  
)
    # html = blocks.RawHTMLBlock()
    class Meta:
        template="streams/richtext.html"
        icon="edit"
        label="RichTextBlock"


class CustomHtml(blocks.StructBlock):
    editor=blocks.TextBlock(required=True)
    class Meta:
        template="streams/ckeditor.html"
        icon="edit"
        label="Custom HTML Editor"

    

class CardBlock(blocks.StructBlock):
    title=blocks.CharBlock(required=True,help_text="Add your Title")
    cards = blocks.ListBlock(
        blocks.StructBlock(
    [

        ("Image", ImageChooserBlock(required=True)),
        ("title", blocks.CharBlock(required=True)),
        ("text", blocks.TextBlock(required=True)),
        ("button", blocks.PageChooserBlock(required=False)),
        ("button_url", blocks.URLBlock(required=False)),
    ]
    )
    )

    class Meta:
        template ="streams/card_block.html"
        icon="placeholder"
        label="staff cards"

class FourdivBlock(blocks.StructBlock):
    #  cards = blocks.ListBlock(
    #     blocks.StructBlock(
    # [

    #     ("Image", ImageChooserBlock(required=True)),
    #     ("title", blocks.CharBlock(required=True)),
    #     ("text", blocks.TextBlock(required=True)),
    # ]
    # )
    #  )
     class Meta:
        template ="streams/four_div_block_2.html"
        label="four_div_block"
        icon="placeholder"



class ButtonBlock(blocks.StructBlock):
    button= blocks.ListBlock(
        blocks.StructBlock(
            [
                ("button_text", blocks.CharBlock(required=True)),
                ("button_url", blocks.URLBlock(required=False)),
            ]
    )
    )
    class Meta:
        template ="streams/button-block.html"
        label="button-block"
        icon="placeholder"

class FooterBlock(blocks.StructBlock):
     footer = blocks.ListBlock(
        blocks.StructBlock(
    [

        ("Image", ImageChooserBlock(required=True)),
        ("title", blocks.CharBlock(required=True)),
        ("text", blocks.TextBlock(required=True)),
        ("ul_title", blocks.CharBlock(required=True)),
    ]
    )
     )
     class Meta:
        template ="streams/footer.html"
        label="footer"
        icon="placeholder"

class LeaderBoardSection(blocks.StructBlock):
    
    class Meta:
        template ="streams/leader_board.html"
        label="leaderboard_section"
        icon="placeholder"


class TestimonialSlider(blocks.StructBlock):
    testimonialslider= blocks.ListBlock(
        blocks.StructBlock(
            [
               ("caption", blocks.TextBlock()),
               ("username", blocks.TextBlock()),
               ("proffesion", blocks.TextBlock()),
               ("rating",blocks.TextBlock()),
    ]
    )
    )
    class Meta:
        template ="streams/testimonial.html"
        label="testimonialslider"
        icon="placeholder"


class Banner(blocks.StructBlock):
    banner= blocks.ListBlock(
        blocks.StructBlock(
            [
            ("banner_image", ImageChooserBlock(required=True)),
            ("banner_overlay_image", ImageChooserBlock(required=True)),
            ("banner_overlay_text_block1", blocks.TextBlock(required=True)),
            ("banner_overlay_text_block2", blocks.TextBlock(required=True)),
            ("banner_overlay_text_block3", blocks.TextBlock(required=True)),
            ("banner_button_1", blocks.TextBlock(required=True)),
            ("banner_button_url_1", blocks.TextBlock(required=True)),
            ("banner_button_2", blocks.TextBlock(required=True)),
            ("banner_button_url_2", blocks.TextBlock(required=True)),
            ]
        )
    )

    class Meta:
        template ="streams/banner.html"
        label="banner"
        icon="placeholder"


class VolunteerBlock(blocks.StructBlock):
    volunteer= blocks.ListBlock(
        blocks.StructBlock(
            [
            ("icon", ImageChooserBlock(required=True)),
            ("volunteers", blocks.TextBlock(required=True)),
            ("text", blocks.TextBlock(required=True)),
            ]
        )
    )


    class Meta:
        template ="streams/volunteer.html"
        label="volunteer"
        icon="placeholder"


class DivSectionBlock(blocks.StructBlock):
    divsection= blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.TextBlock(required=True)),
                ("subtitle", blocks.TextBlock(required=True)),
                ("divsection_image", ImageChooserBlock(required=True)),
            ]
        )
    )

    class Meta:
        template ="streams/divsection.html"
        label="divsection"
        icon="placeholder"


class StudentandEducatorblock(blocks.StructBlock):
    studenteducator= blocks.ListBlock(
        blocks.StructBlock(
            [
                ("heading_student", blocks.TextBlock(required=True)),
                ("sub_heading_student", blocks.TextBlock(required=True)),
                ("button_text_student", blocks.TextBlock(required=True)),
                ("button_1_url", blocks.TextBlock(required=True)),
                ("heading_educator", blocks.TextBlock(required=True)),
                ("sub_heading_educator", blocks.TextBlock(required=True)),
                ("button_text_educator", blocks.TextBlock(required=True)),
                ("button_2_url", blocks.TextBlock(required=True)),

            ]
        )
    )

    class Meta:
        template ="streams/studentandeducator.html"
        label="studentandeducator"
        icon="placeholder"


class Banner_Image_Section2(blocks.StructBlock):
    banner_section_2= blocks.ListBlock(
        blocks.StructBlock(
            [
                ("banner_image", ImageChooserBlock(required=True)),
                ("banner_overlay_text", blocks.TextBlock(required=True)),

            ]
    )
    )

    class Meta:
        template ="streams/bannersectio2.html"
        label="bannersection2"
        icon="placeholder"


class RegisterForm(blocks.StructBlock):
    class Meta:
        template ="streams/staticform.html"
        label=" Educator Register Form"
        icon="placeholder"    

class StudentForm(blocks.StructBlock):
    class Meta:
        template ="streams/studentform.html"
        label=" Student Register Form"
        icon="placeholder"    



class VerticalImagewithTextBlock(blocks.StructBlock):
     vertical = blocks.ListBlock(
        blocks.StructBlock(
    [

        ("Image", ImageChooserBlock(required=True)),
        ("text", blocks.TextBlock(required=True)),
    ]
    )
     )
     class Meta:
        template ="streams/verticalimagewithtext.html"
        label="verticalimagewithtext"
        icon="placeholder"
    
class Signthispetetionform(blocks.StructBlock):
    class Meta:
        template ="streams/signthispetetionform.html"
        label="signthispetetionform"
        icon="placeholder"





class StudentAchivmentBlock(blocks.StructBlock):
     achivment = blocks.ListBlock(
        blocks.StructBlock(
    [

         ("heading_one", blocks.TextBlock(required=True)),
         ("achivment_scores_one", blocks.TextBlock(required=True)),
         ("heading_two", blocks.TextBlock(required=True)),
         ("achivment_scores_two", blocks.TextBlock(required=True)),
         ("heading_three", blocks.TextBlock(required=True)),
         ("achivment_scores_three", blocks.TextBlock(required=True)),
        
    ]
    )
     )
     class Meta:
         template="streams/student_achivments.html"
         label="AchievementBlock"
         icon="placeholder"

WAGTAILADMIN_RICH_TEXT_EDITORS = {
    'default': {
        'WIDGET': 'wagtail.admin.rich_text.DraftailRichTextArea',
        # since sub, super, and a couple more are not included by default, we need to add them in this config
        'OPTIONS': {'features': ['bold', 'italic', 'superscript', 'subscript', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul',
                        'hr', 'blockquote', 'pre', 'link', 'embed', 'document-link', 'image']}
    },
    'minimal': {
        'OPTIONS': {
            'features': ['bold', 'italic', 'subscript', 'superscript', 'link']
        }
    }
}