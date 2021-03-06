# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'GlobalInfo.maps_id'
        db.alter_column(u'consent_management_globalinfo', 'maps_id', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))

        # Changing field 'GlobalInfo.how_to_get_there'
        db.alter_column(u'consent_management_globalinfo', 'how_to_get_there', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'GlobalInfo.consultant_name'
        db.alter_column(u'consent_management_globalinfo', 'consultant_name', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'GlobalInfo.maps_id'
        db.alter_column(u'consent_management_globalinfo', 'maps_id', self.gf('django.db.models.fields.CharField')(max_length=32))

        # Changing field 'GlobalInfo.how_to_get_there'
        db.alter_column(u'consent_management_globalinfo', 'how_to_get_there', self.gf('django.db.models.fields.TextField')(default='a'))

        # Changing field 'GlobalInfo.consultant_name'
        db.alter_column(u'consent_management_globalinfo', 'consultant_name', self.gf('django.db.models.fields.TextField')(default='a'))

    models = {
        u'consent_management.globalinfo': {
            'Meta': {'object_name': 'GlobalInfo'},
            'consultant_name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'how_to_get_there': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maps_id': ('django.db.models.fields.CharField', [], {'default': "'ChIJz3g54adeeUgRMRGZkTY7BKk'", 'max_length': '32', 'null': 'True', 'blank': 'True'})
        },
        u'consent_management.procedure': {
            'ICD9_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            'Meta': {'object_name': 'Procedure'},
            'alternative_names': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'consent_form': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['consent_management.ProcedureDetails']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'extra_procedures': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['consent_management.Procedure']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'consent_management.proceduredetails': {
            'Meta': {'object_name': 'ProcedureDetails'},
            'after_care': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'anaesthesia': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'explanation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'follow_up': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recovery': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['consent_management']