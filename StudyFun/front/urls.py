from django.conf.urls import url
from django.urls import path

from . import views # import views so we can use them in urls.

urlpatterns = [
    url(r'^$', views.index),
    path('home/', views.index, name="home"),
    path('settings/', views.settingsPage, name="settings"),
    path('statistics/', views.statisticsPage, name="statistics"),
    path('help/', views.helpPage, name="help"),
]