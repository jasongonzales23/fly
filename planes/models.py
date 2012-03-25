from django.db import models

class Fleet(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('fleet_view', args=[self.pk])
    class Meta:
        verbose_name_plural = 'fleet'

class Plane(models.Model):
    fleet = models.ForeignKey(Fleet)
    order = models.IntegerField()
    image = models.ImageField(upload_to="uploads/planeImages")
    title = models.CharField(max_length=255, blank=True)
    seats = models.CharField(max_length=255, blank=True)
    range = models.CharField(max_length=255, blank=True)
    speed = models.CharField(max_length=255, blank=True)
    ceiling = models.CharField(max_length=255, blank=True)
    description = models.TextField(max_length=255, blank=True )

    class Meta:
        ordering = ["order"]
    
    def __unicode__(self):
        return str(self.order)

#stuff you need to make it a plugin
from cms.models import CMSPlugin

class FleetPlugin(CMSPlugin):
    fleet = models.ForeignKey('planes.Fleet', related_name='plugins')
    
    def __unicode__(self):
        return self.fleet.name

