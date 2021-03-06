from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    url(r'^HomePage/', include('HomePage.urls'), name='HomePage'),
    url(r'^Skills/', include('Skills.urls'), name='Skills'),
    url(r'^Education/', include('Education.urls'), name='Education'),
    url(r'^Portfolio/', include('Portfolio.urls'), name='Portfolio'),
    url(r'^AboutMe/', include('AboutMe.urls'), name='AboutMe'),
    url(r'^Experience/', include('Experience.urls'), name='Experience'),
    url(r'^Blog/', include('Blog.urls'), name='Blog')
]

