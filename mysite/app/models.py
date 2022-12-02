from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)

from streams import blocks

# Create y our models here.

class FlexPage(Page):
    template= "app/flex_page.html"
    content = StreamField(
        [
            ("title_and_text" , blocks.TitleAndTextBlock()),
            ("richtext", blocks.RichTextBlock()),
            ("card",blocks.CardBlock()),
            ("fourdiv", blocks.FourdivBlock()),
            ("footer", blocks.FooterBlock()),
            ("Button", blocks.ButtonBlock()),
            ("leaderboardsection",blocks.LeaderBoardSection()),
            ("testimonialslider",blocks.TestimonialSlider()),
            ("banner",blocks.Banner()),
            ("volunteer",blocks.VolunteerBlock()),
            ("divsection",blocks.DivSectionBlock()),
            ("studentandeducator", blocks.StudentandEducatorblock()),
            ("banner_section_2", blocks.Banner_Image_Section2()),
            ("staticform",blocks.RegisterForm()),
            ("four_div_block_2",blocks.FourdivBlock2()),
            
   
            # ("cta",blocks.CtaBlock()),
        ],
        null=True,
        blank=True
     )
    subtitle= models.CharField(max_length=255, null= True , blank=True)
    content_panels= Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),

    ]

    class Meta:
        verbose_name= "FlexPage"
        verbose_name_plural="Flex Pages"


    # @register_setting
    # class SiteSettings(BaseSetting):
    #     logo = models.OneToOneField(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name=' logo')
    #     panels = [
    #         ImageChooserPanel('logo'),
    #     ]
            
class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class ContactPage(AbstractEmailForm):

    template = "app/flex_page.html"
    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    # landing_page_template = "app/flex_page.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
    ]

register_snippet(FormField)
register_snippet(ContactPage)