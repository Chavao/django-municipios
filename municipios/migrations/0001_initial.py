# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UF'
        db.create_table(u'municipios_uf', (
            ('id_ibge', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('uf', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('regiao', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'municipios', ['UF'])

        # Adding model 'Municipio'
        db.create_table(u'municipios_municipio', (
            ('id_ibge', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('nome_abreviado', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('uf', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['municipios.UF'])),
            ('uf_sigla', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'municipios', ['Municipio'])


    def backwards(self, orm):
        # Deleting model 'UF'
        db.delete_table(u'municipios_uf')

        # Deleting model 'Municipio'
        db.delete_table(u'municipios_municipio')


    models = {
        u'municipios.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'id_ibge': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nome_abreviado': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['municipios.UF']"}),
            'uf_sigla': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'municipios.uf': {
            'Meta': {'object_name': 'UF'},
            'id_ibge': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'regiao': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'uf': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['municipios']
