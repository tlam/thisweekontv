# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Show'
        db.create_table('shows_show', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('tvdb_id', self.gf('django.db.models.fields.IntegerField')()),
            ('season', self.gf('django.db.models.fields.IntegerField')()),
            ('last_seen', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('shows', ['Show'])


    def backwards(self, orm):
        # Deleting model 'Show'
        db.delete_table('shows_show')


    models = {
        'shows.show': {
            'Meta': {'object_name': 'Show'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_seen': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'season': ('django.db.models.fields.IntegerField', [], {}),
            'tvdb_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['shows']