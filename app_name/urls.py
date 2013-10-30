from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', '{{ app_name }}.views.pages.home'),
    url(r'basic/$', '{{ app_name }}.views.pages.basic'),
    url(r'hybrid/$', '{{ app_name }}.views.pages.hybrid'),
        
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
)
