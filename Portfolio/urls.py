from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Post/', views.post, name='post'),
    url(r'Submit/', views.post, name='submit'),
    url(r'PortfolioShow/', views.Portfolio_Show, name='Show')
]

