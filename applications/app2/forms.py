# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import BeritaModel

# Create your forms here.

class BeritaForm(ModelForm):
    class Meta:
        # model yang akan digunakan dalam form
        model = BeritaModel

        # semua fields digunakan dalam form,
        # kecuali id_sumber_berita tidak ditampilkan pada form
        exclude = ['id_sumber_berita']
