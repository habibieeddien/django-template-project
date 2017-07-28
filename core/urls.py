"""django_project_template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from applications.app1 import views as app1
from applications.app2 import views as app2
from applications.app3 import views as app3

urlpatterns = [
    url(r'^$', app1.index, name='index'),
    url(r'^app2/', app2.index, name='index'),
    url(r'^app3/', app3.index, name='index'),
    url(r'^success/', app2.success, name='success'),
    url(r'^list/report', app2.list_laporan, name='berita-list-view'),
]
