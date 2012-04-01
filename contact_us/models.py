from django.db import models
from django.forms import ModelForm
from django import forms
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from datetime import datetime

INTEREST_CHOICES = (
    ('fly_management','FLY Management'),
    ('shared_ownership','Shared Ownership'),
    ('acquisition','Acquisition'),
)

class Contact(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email= models.EmailField(max_length=255)
    phone= models.CharField(max_length=30, blank=True)
    interest= models.CharField(max_length=255, verbose_name="I'm interested in (optional)", blank=True)
    application_date= models.DateTimeField(auto_now_add=True)
    #status = models.CharField(max_length=255, choices= STATUS, default="active")
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.interest)


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'phone', 'interest')
        widgets = {
            'interest': CheckboxSelectMultiple(choices=INTEREST_CHOICES, attrs={'class': 'checkbox',})
        }
    


