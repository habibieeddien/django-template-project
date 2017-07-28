# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models

# Create your models here.
from django.views.generic.list import ListView

class ImageBeritaModel(models.Model):
    """
    DBTable ImageBeritaModel
    """
    # PK dan auto-increament
    id_gambar = models.AutoField(primary_key=True)
    gambar = models.ImageField(null=True, upload_to='static/uploads/')

    def __str__(self):
        # id_gambar sebagai PK dan
        # FK ke model lain
        return self.gambar


class BeritaModel(models.Model):
    """
    DBTable BeritaModel
    """
    SUMBER_BERITA = (
        ('WAGR', 'WAG Riau'),
        ('WAGJ', 'WAG Jambi'),
        ('WAGKALTENG', 'WAG Kalteng'),
    )
    JENIS_EVENT = (
        ('F', 'Firespot'),
        ('H', 'Hotspot'),
        ('K', 'Karhutla'),
    )
    id_form_berita = models.AutoField(primary_key=True)
    sumber = models.CharField(max_length=10, choices=SUMBER_BERITA)
    kontak = models.CharField(max_length=15, null=True)
    isi_berita = models.TextField(blank=False, null=False)
    jenis_kejadian = models.CharField(max_length=1, choices=JENIS_EVENT)
    waktu_kejadian = models.DateTimeField(default=datetime.datetime.now)
    gambar = models.ForeignKey(ImageBeritaModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        # id_form_berita
        return self.id_form_berita

class BeritaListView(ListView):
    """
    untuk menampilkan rekap Berita dari DB
    """
    model = BeritaModel
    template_name = 'app2/list_laporan.html'

    def get_context_data(self, **kwargs):
        context = super(BeritaListView, self).get_context_data(**kwargs)
        return context
