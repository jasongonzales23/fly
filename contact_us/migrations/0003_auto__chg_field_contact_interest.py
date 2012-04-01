# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Contact.interest'
        db.alter_column('contact_us_contact', 'interest', self.gf('django.db.models.fields.CharField')(max_length=255))


    def backwards(self, orm):
        
        # Changing field 'Contact.interest'
        db.alter_column('contact_us_contact', 'interest', self.gf('django.db.models.fields.CharField')(max_length=30))


    models = {
        'contact_us.contact': {
            'Meta': {'object_name': 'Contact'},
            'application_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        }
    }

    complete_apps = ['contact_us']
