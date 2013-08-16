from django.conf.urls import patterns, include, url
from dyndns import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'djDyndns.views.home', name='home'),
    # url(r'^djDyndns/', include('djDyndns.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Dyndns
    url(r'^$', views.index, name='index')
)
