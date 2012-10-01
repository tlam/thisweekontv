# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Episode'
        db.create_table('episodes_episode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('show', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shows.Show'])),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('air_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('episodes', ['Episode'])


    def backwards(self, orm):
        # Deleting model 'Episode'
        db.delete_table('episodes_episode')


    models = {
        'episodes.episode': {
            'Meta': {'object_name': 'Episode'},
            'air_date': ('django.db.models.fields.DateField', [], {}),
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