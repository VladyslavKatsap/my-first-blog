from django.template.defaulttags import url
from . import views
from django.urls import path

urlpatterns = [
    path(r'', views.post_list, name='post_list'),
]