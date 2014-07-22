from django.conf.urls import patterns, include, url
from views import PageFactory

urlpatterns = patterns('',
   url(r'^/?$', PageFactory.instance(PageFactory.HOME)),
   url(r'^index.html', PageFactory.instance(PageFactory.HOME)),
   url(r'^status/?', PageFactory.instance(PageFactory.JOB_STATUS)),
   url(r'^results/?', PageFactory.instance(PageFactory.JOB_RESULTS))
)
