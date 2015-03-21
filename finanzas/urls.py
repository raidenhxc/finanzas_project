from django.conf.urls import patterns, url
from finanzas import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
)