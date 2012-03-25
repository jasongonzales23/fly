# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'FleetPlugin'
        db.delete_table('cmsplugin_fleetplugin')


    def backwards(self, orm):
        
        # Adding model 'FleetPlugin'
        db.create_table('cmsplugin_fleetplugin', (
            ('fleet', self.gf('django.db.models.fields.related.ForeignKey')(related_name='plugins', to=orm['planes.Fleet'])),
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('planes', ['FleetPlugin'])


    models = {
        'planes.fleet': {
            'Meta': {'object_name': 'Fleet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'planes.plane': {
            'Meta': {'ordering': "['order']", 'object_name': 'Plane'},
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
