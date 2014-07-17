from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import RequestResultAPI, RequestJobListAPI, RequestJobAPI

urlpatterns = patterns('',
    url(r'^results/(\d+)/?$', RequestResultAPI.as_view(), name="Request Result API View"),
    url(r'^jobs/(\d+)/?$', RequestJobAPI.as_view(), name="Request Job API View"),
    url(r'^jobs/?$', RequestJobListAPI.as_view(), name="Request Job List API View")
)
