from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.http import require_GET

class PageFactory:
    HOME = 'web/index.html'
    JOB_STATUS = 'web/status.html'
    JOB_RESULTS = 'web/results.html'

    def instance(template):
        @require_GET
        def page(request):
            template = loader.get_template(template)
            context = RequestContext(request)
            return HttpResponse(template.render(context))
        return page
