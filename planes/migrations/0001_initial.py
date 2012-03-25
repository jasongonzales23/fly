# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Fleet'
        db.create_table('planes_fleet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('planes', ['Fleet'])

        # Adding model 'Plane'
        db.create_table('planes_plane', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fleet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['planes.Fleet'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('seats', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('range', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('speed', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('ceiling', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('planes', ['Plane'])


    def backwards(self, orm):
        
        # Deleting model 'Fleet'
        db.delete_table('planes_fleet')

        # Deleting model 'Plane'
        db.delete_table('planes_plane')


    models = {
        'planes.fleet': {
            'Meta': {'object_name': 'Fleet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'planes.plane': {
            'Meta': {'object_name': 'Plane'},
            'ceiling': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'fleet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['planes.Fleet']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'range': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'seats': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'speed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['planes']
