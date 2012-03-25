# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Slide.thumbnail'
        db.delete_column('slideshow_slide', 'thumbnail')


    def backwards(self, orm):
        
        # Adding field 'Slide.thumbnail'
        db.add_column('slideshow_slide', 'thumbnail', self.gf('django.db.models.fields.files.ImageField')(default=0, max_length=100), keep_default=False)


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'slideshow.slide': {
            'Meta': {'ordering': "['order']", 'object_name': 'Slide'},
            'buttonLink': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'buttonText': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'caption': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'heading_1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'heading_2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'slide': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slideshow': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['slideshow.Slideshow']"})
        },
        'slideshow.slideshow': {
            'Meta': {'object_name': 'Slideshow'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'slideshow.slideshowplugin': {
            'Meta': {'object_name': 'SlideshowPlugin', 'db_table': "'cmsplugin_slideshowplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'slideshow': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plugins'", 'to': "orm['slideshow.Slideshow']"})
        }
    }

    complete_apps = ['slideshow']
