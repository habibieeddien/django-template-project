# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    body = 'Aplikasi 3'
    return render(request, 'index.html', {'body_html': body})