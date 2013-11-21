from django.conf.urls import patterns, url

from contact import views

urlpatterns = patterns('',
    url(r'^contact/', 'contact.views.contact'),
    url(r'^thanks/', 'contact.views.thanks'),
)