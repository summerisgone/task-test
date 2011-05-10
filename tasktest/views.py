# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView
from pkg_resources import *
from tasks import pip_install_lib


class ReadyView(TemplateView):
    template_name = 'ready.html'

class IndexView(TemplateView):
    template_name = "index.html"

def load(request):
    if request.method == 'POST':
        tasks = []
        for req in request.POST.get('requirements', '').splitlines():
            tasks.append(pip_install_lib.delay(req))
        return render(request, 'loading.html', {'tasks': tasks})
    else:
        return render(request, 'loading.html', {})
