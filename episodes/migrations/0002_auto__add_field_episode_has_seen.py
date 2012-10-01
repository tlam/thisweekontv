# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Episode.has_seen'
        db.add_column('episodes_episode', 'has_seen',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Episode.has_seen'
        db.delete_column('episodes_episode', 'has_seen')


    models = {
        'episodes.episode': {
            'Meta': {'object_name': 'Episode'},
            'air_date': ('django.db.models.fields.DateField', [], {}),
            'has_seen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'show': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shows.Show']"})
        },
        'shows.show': {
            'Meta': {'object_name': 'Show'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_seen': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'season': ('django.db.models.fields.IntegerField', [], {}),
            'tvdb_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['episodes']