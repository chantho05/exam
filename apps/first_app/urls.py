from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home), 
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout), 
    url(r'^dashboard$', views.dashboard),
    url(r'^new$', views.new),
    url(r'^added$', views.added),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^activity/(?P<id>\d+)$', views.activity),
    url(r'^join/(?P<id>\d+)$', views.join),
    url(r'^leave/(?P<id>\d+)$', views.leave),

]