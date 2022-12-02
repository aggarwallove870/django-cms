from django.db import models

# Create your models here.
from django.db import models
from wagtailmenus.models import MenuPage
from django_extensions.db.fields import AutoSlugField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    InlinePanel,
    FieldPanel,
    PageChooserPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet
from wagtailmenus.panels import menupage_panel


from django.db import models

# Create your models here.
from django.db import models
from wagtailmenus.models import MenuPage
from django_extensions.db.fields import AutoSlugField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    InlinePanel,
    FieldPanel,
    PageChooserPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet
from wagtailmenus.panels import menupage_panel

class MenuItem(Orderable):

    link_title = models.CharField(
        blank=True,
        null=True,
        max_length=500
    )
    link_url = models.CharField(
        max_length=500,
        blank=True
    )
    icon = models.CharField(
        max_length=500,blank=True,null=True
    )
    link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,
    )
    social_media_name   = models.CharField(max_length=500, blank=True, null=True)
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    page = ParentalKey("Menu", related_name="menu_items")

    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_url"),
        FieldPanel("icon"),
        # FieldPanel("link_page"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
        FieldPanel("social_media_name"),
        
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return 'Missing Title'


@register_snippet
class Menu(ClusterableModel):
    """The main menu clusterable model."""

    title = models.CharField(max_length=100)
   
    slug = AutoSlugField(populate_from="title", editable=True)
    # slug = models.SlugField()

    panels = [
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("slug"),
        ], heading="Menu"),
        InlinePanel("menu_items", label="Menu Item")
    ]

    def __str__(self):
        return self.title



@register_snippet
class NavbarLogo(models.Model):
    name=models.CharField(max_length=255)
    logo=models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE , related_name="+"
)
    panels = [
        FieldPanel('name',classname='full'),
        ImageChooserPanel('logo'),
    ]

# @register.simple_tag(takes_context=True)
# def get_all_pages(context):
#     return Page.objects.live()


def __str__(self):
    return self.name


@register_snippet
class Footer(Orderable):
    footer_icon_title = models.CharField(
        blank=True,
        null=True,
        max_length=500
    )
    footer_paragraph = models.TextField(blank=True, null=True)
    logo=models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE , related_name="+", null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    footer_social_menu = models.ForeignKey(Menu, null=True, blank=True,on_delete=models.CASCADE)
 
    panels = [
        FieldPanel('footer_icon_title'),
        FieldPanel('footer_paragraph'),
        FieldPanel('phone'),
        FieldPanel('address'),
        FieldPanel('email'),
        ImageChooserPanel('logo'),
        PageChooserPanel('footer_social_menu')
    
    ]


def __str__(self):
    return self.footer_icon_title
   

   