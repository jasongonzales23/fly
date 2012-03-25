from django.db import models
#from django import forms
#from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
#from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

class Slideshow(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('slideshow_view', args=[self.pk])
    class Meta:
        verbose_name_plural = 'slideshow'
    
class Slide(models.Model):
    slideshow = models.ForeignKey(Slideshow)
    order = models.IntegerField()
    slide = models.ImageField(upload_to="uploads/slideshowImages/")
    heading_1 = models.CharField(max_length=50, blank=True)
    heading_2 = models.CharField(max_length=50, blank=True)
    caption = models.TextField(max_length=255, blank=True)
    buttonText = models.CharField(max_length=50, blank=True)
    buttonLink = models.CharField(max_length=50, blank=True)
    
    class Meta:
        ordering = ["order"]
    
    def __unicode__(self):
        return str(self.order)

#stuff you need to make it a plugin
from cms.models import CMSPlugin

class SlideshowPlugin(CMSPlugin):
    slideshow = models.ForeignKey('slideshow.Slideshow', related_name='plugins')
    
    def __unicode__(self):
        return self.slideshow.name

