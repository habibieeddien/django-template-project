"""
Module views APP2
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import BeritaForm
from .models import BeritaListView

# Create your views here.

def index(request):
    """
    URL untuk Form Laporan
    """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BeritaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            # simpan ke DB
            form.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/success/')

    # if a GET (or any other method) we'll create a blank form
    else:
        # jika bukan method POST, maka kirim blank form
        form = BeritaForm()

    return render(request, 'app2/wagform.html', {'form_html': form})

def success(request):
    """
    Jika method POST success, redirect ke URL ini
    """
    return render(request, 'app2/success.html')

def list_laporan(request):
    """
    Request rekap laporan yang tersedia di DB
    """
    report_list = BeritaListView.as_view()
    return render(request, report_list)#'app2/list_laporan.html', {'list_html' : report_list})
