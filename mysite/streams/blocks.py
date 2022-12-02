from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import PageChooserBlock
from wagtail.images.apps import WagtailImagesAppConfig


  
class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True,help_text="Title")
    text = blocks.TextBlock(required=True,help_text="Text")
    class Meta:
        template ="streams/title_and_text.html"
        icon="edit"
        label= "Title and Text"


class RichTextBlock(blocks.RichTextBlock):
    class Meta:
        template="streams/richtext.html"
        icon="edit"
        label="RichTextBlock"


class CardBlock(blocks.StructBlock):
    title=blocks.CharBlock(required=True,help_text="Add your Title")
    cards = blocks.ListBlock(
        blocks.StructBlock(
    [

        ("Image", ImageChooserBlock(required=True)),
        ("title", blocks.CharBlock(required=True, max_length=40)),
        ("text", blocks.TextBlock(required=True,max_length=50)),
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
     cards = blocks.ListBlock(
        blocks.StructBlock(
    [

        ("Image", ImageChooserBlock(required=True)),
        ("title", blocks.CharBlock(required=True, max_length=40)),
        ("text", blocks.TextBlock(required=True,max_length=50)),
    ]
    )
     )
     class Meta:
        template ="streams/four_div_block.html"
        label="four_div_block"
        icon="placeholder"



class ButtonBlock(blocks.StructBlock):
    button= blocks.ListBlock(
        blocks.StructBlock(
            [
                ("button_text", blocks.CharBlock(required=True, max_length=50)),
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
        ("title", blocks.CharBlock(required=True, max_length=40)),
        ("text", blocks.TextBlock(required=True,max_length=50)),
        ("ul_title", blocks.CharBlock(required=True, max_length=40)),
    ]
    )
     )
     class Meta:
        template ="streams/footer.html"
        label="footer"
        icon="placeholder"

class LeaderBoardSection(blocks.StructBlock):
    leaderboardsection= blocks.ListBlock(
        blocks.StructBlock(
            [
               ("leader_image", ImageChooserBlock(required=True)),
               ("leader_name", blocks.TextBlock(required=True, max_length=300)),
               ("leader_university_name", blocks.TextBlock(required=True, max_length=300)),
               ("leader_university_address", blocks.TextBlock(required=True, max_length=300))   
    ]
    )
    )
    class Meta:
        template ="streams/leader_board.html"
        label="leaderboard_section"
        icon="placeholder"


class TestimonialSlider(blocks.StructBlock):
    testimonialslider= blocks.ListBlock(
        blocks.StructBlock(
            [
            #    ("image", ImageChooserBlock(required=True)),
               ("caption", blocks.TextBlock(required=True, max_length=300)),
               ("username", blocks.TextBlock(required=True, max_length=300)),
               ("proffesion", blocks.TextBlock(required=True, max_length=300)),
               ("rating",blocks.TextBlock(required=True, max_length=100)),
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
            ("volunteers", blocks.TextBlock(required=True, max_length=100)),
            ("text", blocks.TextBlock(required=True, max_length=100)),
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
                ("title", blocks.TextBlock(required=True, max_length=100)),
                ("subtitle", blocks.TextBlock(required=True, max_length=100)),
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
                ("heading_student", blocks.TextBlock(required=True, max_length=100)),
                ("sub_heading_student", blocks.TextBlock(required=True, max_length=100)),
                ("button_text_student", blocks.TextBlock(required=True, max_length=100)),
                ("heading_educator", blocks.TextBlock(required=True, max_length=100)),
                ("sub_heading_educator", blocks.TextBlock(required=True, max_length=100)),
                ("button_text_educator", blocks.TextBlock(required=True, max_length=100)),

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
                ("banner_overlay_text", blocks.TextBlock(required=True, max_length=100)),

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
        label="Register Form"
        icon="placeholder"    


class FourdivBlock2(blocks.StructBlock):
     cards = blocks.ListBlock(
        blocks.StructBlock(
    [

        ("Image", ImageChooserBlock(required=True)),
        ("title", blocks.CharBlock(required=True)),
        ("text", blocks.TextBlock(required=True)),
    ]
    )
     )
     class Meta:
        template ="streams/four_div_block_2.html"
        label="four_div_block_2"
        icon="placeholder"

