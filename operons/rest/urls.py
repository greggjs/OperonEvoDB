from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import ResultAPI, JobListAPI, JobAPI

urlpatterns = patterns('',
    url(r'^results/(\d+)/?$', ResultAPI.as_view(), name="Request Result API View"),
    url(r'^jobs/(\d+)/?$', JobAPI.as_view(), name="Request Job API View"),
    url(r'^jobs/?$', JobListAPI.as_view(), name="Request Job List API View")
)
