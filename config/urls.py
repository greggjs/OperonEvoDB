from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('operons.web.urls'), name='home'),
    url(r'^rest/', include('operons.rest.urls'), name='api'),
    url(r'^admin/', include(admin.site.urls)),
)
