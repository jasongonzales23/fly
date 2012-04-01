# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Contact'
        db.create_table('contact_us_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('interest', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('application_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('contact_us', ['Contact'])


    def backwards(self, orm):
        
        # Deleting model 'Contact'
        db.delete_table('contact_us_contact')


    models = {
        'contact_us.contact': {
            'Meta': {'object_name': 'Contact'},
            'application_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        }
    }

    complete_apps = ['contact_us']
