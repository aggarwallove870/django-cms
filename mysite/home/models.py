from django.db import models
from wagtail.core.models import Page
from wagtail.models import Page, Orderable
from django import forms
from wagtail.admin.edit_handlers import FieldPanel ,MultiFieldPanel, InlinePanel,FieldRowPanel
from wagtail.core.fields import RichTextField
from wagtail.admin.panels import PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Collection, Page
from wagtail.images import get_image_model
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from menu.models import MenuItem
from modelcluster.fields import ParentalKey

from wagtail.fields import StreamField
from wagtail.admin.panels import StreamFieldPanel

class CarouselItem(Orderable):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    caption = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=True)
    proffesion= models.CharField(max_length=255, blank=True)
    page = ParentalKey('HomePage', related_name='carousel_items')

    panels = [
    ImageChooserPanel('image'),
    FieldPanel('caption'),
    FieldPanel('proffesion'),
    FieldPanel('username'),
    ]

class Leaderboard(models.Model):
    leader_name=models.CharField(max_length=100,null=True,blank=True)
    leader_image = models.ForeignKey("wagtailimages.Image", on_delete=models.SET_NULL, null=True, blank=True, related_name="+")
    leader_university_name=models.CharField(max_length=100,null=True,blank=True)
    leader_university_address=models.CharField(max_length=100,null=True,blank=True)


            
    panels=[
        MultiFieldPanel(
        [
            FieldPanel('leader_name'),
            ImageChooserPanel('leader_image'),
            FieldPanel('leader_university_name'),
            FieldPanel('leader_university_address'),
    ],
    heading = 'Leaderborad-Detail',
    )
    ]

    def __str__(self):
        return self.leader_name


    class Meta:
            verbose_name = "Image Gallery"


    

    
        
register_snippet(Leaderboard)

class HomePage(Page): 
    '''Home page for  Models'''
    templates = "home/home_page.html"
    def  get_context(self,request,*args,**kwargs):
        context= super(HomePage,self).get_context(request,*args,**kwargs)  
        context["imgglry"]=Leaderboard.objects.all()
        # context['menumy']=MenuItem.objects.all()
        
        return context

    max_count = 1
    banner_title = models.CharField(max_length=100,blank=False,null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image= models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    
    )
    banner_overlay_text= RichTextField()
    banner_overlay_image= models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    
    )
    banner_button_first= models.CharField(max_length=100, blank=True, null=True)
    banner_button_first_url= models.URLField(max_length=100, blank=True)
    banner_button_second= models.CharField(max_length=100, blank=True, null=True)
    banner_button_second_url= models.URLField(max_length=100, blank=True)
    heading_of_section_1 = RichTextField()
    subheading_of_section_1 = RichTextField()
    image_of_section_1= models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    
    )
    volunteers_box1_section_2 = models.CharField(max_length=100, blank=True, null=True)
    volunteers_box1_image_section_2= models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    
    )
    volunteers_box1_text_section_2 = models.CharField(max_length=100, blank=True, null=True)
    volunteers_box2_section_2 = models.CharField(max_length=100, blank=True, null=True)
    volunteers_box2_image_section_2= models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    
    )
    volunteers_box2_text_section_2 = models.CharField(max_length=100, blank=True, null=True)
    volunteers_box3_section_2 = models.CharField(max_length=100, blank=True, null=True)
    volunteers_box3_image_section_2= models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    
    )
    volunteers_box3_text_section_2 = models.CharField(max_length=100, blank=True, null=True)
    volunteers_box4_section_2 = models.CharField(max_length=100, blank=True, null=True)
    volunteers_box4_image_section_2= models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    
    )
    volunteers_box4_text_section_2 = models.CharField(max_length=100, blank=True, null=True)
    # carousel_field = StreamField(
    #         [
    #             ('carousel',Carousel()),

    #         ],blank = True
    #     )
    def something(self):
        return self.banner_title

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        FieldPanel("banner_overlay_text"),
        ImageChooserPanel("banner_image"),
        ImageChooserPanel("banner_overlay_image"),
        FieldPanel("banner_button_first"),
        FieldPanel("banner_button_first_url"),
        FieldPanel("banner_button_second"),
        FieldPanel("banner_button_second_url"),
        FieldPanel("heading_of_section_1"),
        FieldPanel("subheading_of_section_1"),
        ImageChooserPanel("image_of_section_1"),
        FieldPanel("volunteers_box1_section_2"),
        ImageChooserPanel("volunteers_box1_image_section_2"),
        FieldPanel("volunteers_box1_text_section_2"),
        FieldPanel("volunteers_box2_section_2"),
        ImageChooserPanel("volunteers_box2_image_section_2"),
        FieldPanel("volunteers_box2_text_section_2"),
        FieldPanel("volunteers_box3_section_2"),
        ImageChooserPanel("volunteers_box3_image_section_2"),
        FieldPanel("volunteers_box3_text_section_2"),
        FieldPanel("volunteers_box4_section_2"),
        ImageChooserPanel("volunteers_box4_image_section_2"),
        FieldPanel("volunteers_box4_text_section_2"),
        InlinePanel('carousel_items', label="Carousel Items"),
        # FieldRowPanel([
        #     FieldPanel("volunteers_box2_text_section_2"),
        #     FieldPanel("volunteers_box3_section_2"),
        
        # ]),

        # StreamFieldPanel('carousel_field'),      

    ]


    class Meta:
        verbose_name="HomePage"





# class ImageGalleryBlock(blocks.StructBlock):
#         image = ImageChooserBlock()
#         text = blocks.RichTextBlock(blank=True)

#         class Meta:
#             template = 'streams/image_gallery.html'

# class Carousel(blocks.StructBlock):
#         carousel = blocks.ListBlock(ImageGalleryBlock(),blank = True)

#         class Meta:
#             template = 'streams/image_gallery.html'



