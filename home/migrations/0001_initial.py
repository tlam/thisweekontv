# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TVConfiguration'
        db.create_table('home_tvconfiguration', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('api_key', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('home', ['TVConfiguration'])


    def backwards(self, orm):
        # Deleting model 'TVConfiguration'
        db.delete_table('home_tvconfiguration')


    models = {
        'home.tvconfiguration': {
            'Meta': {'object_name': 'TVConfiguration'},
            'api_key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['home']