from django.http import HttpResponse
from django.template import loader

from .models import Project

def index(request):
    project_list = Project.objects.order_by('-code')
    template = loader.get_template('core/index.html')
    context = {
        'project_list': project_list,
    }
    return HttpResponse(template.render(context, request))