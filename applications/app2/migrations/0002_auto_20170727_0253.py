# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 02:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeritaModel',
            fields=[
                ('id_form_berita', models.AutoField(primary_key=True, serialize=False)),
                ('sumber', models.CharField(choices=[('WAGR', 'WAG Riau'), ('WAGJ', 'WAG Jambi'), ('WAGKALTENG', 'WAG Kalteng')], max_length=10)),
                ('kontak', models.CharField(max_length=15, null=True)),
                ('isi_berita', models.TextField()),
                ('jenis_kejadian', models.CharField(choices=[('WAGR', 'WAG Riau'), ('WAGJ', 'WAG Jambi'), ('WAGKALTENG', 'WAG Kalteng')], max_length=1)),
                ('waktu_kejadian', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='ImageBerita',
            new_name='ImageBeritaModel',
        ),
        migrations.RemoveField(
            model_name='formberita',
            name='gambar',
        ),
        migrations.DeleteModel(
            name='FormBerita',
        ),
        migrations.AddField(
            model_name='beritamodel',
            name='gambar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app2.ImageBeritaModel'),
        ),
    ]
