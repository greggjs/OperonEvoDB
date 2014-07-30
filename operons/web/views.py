from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.http import require_GET
import os

class Page:
    def __init__(self, head, body, script, title):
        self._head = head
        self._body = body
        self._script = script
        self._title

    @staticmethod
    def fromGroup(group):
        prefix = 'web/' + group + '/'
        head = prefix + 'head.html'
        body = prefix + 'body.html'
        title = group[0].upper() + group[1:]
        script = 'operons/pages/' + group + '.js'
        return Page(head, body, script, title)

    def head(self):
        return self._head

    def body(self):
        return self._body

    def title(self):
        return self._title

    def script(self):
        script_dict = { 'script' : self._script }
        return loader.render_to_string('web/base/script.html', script_dict)


class PageFactory:
    HOME = Page.fromGroup('search')
    JOB_STATUS = Page.fromGroup('status')
    JOB_RESULTS = Page.fromGroup('results')

    def instance(page):
        @require_GET
        def page(request):
            context = RequestContext(request)
            body = loader.render_to_string(page.body(), {}, context)
            head = '' if not page.head() else loader.render_to_string(page.head(), {}, context)
            app = loader.get_template('web/base/app.html')
            args = {
                'body' : body,
                'title' : page.title(),
                'head' : head,
                'script': page.script()
            }
        return page
