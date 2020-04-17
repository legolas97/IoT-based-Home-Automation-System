from django.conf.urls import url,include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.urls import path

#from .views import FileView
app_name = 'nextapp'

urlpatterns = [

    path('ajax_update_relay_status/', views.ajax_update_relay_status, name='ajax_update_relay_status'),
    path('get_relay_group_status/', views.get_relay_group_status, name='get_relay_group_status'),
    path('relay_items/', views.relay_items, name='relay_items'),


]
