from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    url(r'^HomePage/', include('HomePage.urls'), name='HomePage'),
    url(r'^Skills/', include('Skills.urls'), name='Skills'),
    url(r'^Education/', include('Education.urls'), name='Education')
]

