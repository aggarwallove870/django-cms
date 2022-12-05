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
        template ="streams/four_div_block.html"
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
    leaderboardsection= blocks.ListBlock(
        blocks.StructBlock(
            [
               ("leader_image", ImageChooserBlock(required=True)),
               ("leader_name", blocks.TextBlock(required=True)),
               ("leader_university_name", blocks.TextBlock(required=True)),
               ("leader_university_address", blocks.TextBlock(required=True))   
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
               ("caption", blocks.TextBlock(required=True)),
               ("username", blocks.TextBlock(required=True)),
               ("proffesion", blocks.TextBlock(required=True)),
               ("rating",blocks.TextBlock(required=True)),
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
                ("heading_educator", blocks.TextBlock(required=True)),
                ("sub_heading_educator", blocks.TextBlock(required=True)),
                ("button_text_educator", blocks.TextBlock(required=True)),

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

