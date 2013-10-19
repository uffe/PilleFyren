from django.conf.urls import patterns, include, url
from datalogger.models import LogEntry, Filling

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^api/filling/$', 'datalogger.views.registerFilling'),
    url(r'^api/log/$', 'datalogger.views.registerLog'),
    # url(r'^$', 'PilleFyren.views.home', name='home'),
    # url(r'^PilleFyren/', include('PilleFyren.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
