from django.conf.urls import url
from django.urls import path

from . import views # import views so we can use them in urls.

urlpatterns = [
    url(r'^$', views.index),
    path('home/', views.index, name="home"),
    path('settings/', views.settings_page, name="settings"),
    path('statistics/', views.statistics_page, name="statistics"),
    path('help/', views.help_page, name="help"),
    path('stacks/', views.manage_stacks_page, name="stacksPage"),
    path('insert_stack/', views.insert_stack, name="stackInsertingPage"),
    path('delete_stack/<int:stack_id>/', views.delete_stack, name="stackDeletingPage"),
]
