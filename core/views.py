from django.http import HttpResponse
from django.template import loader

from .models import Project
from .tables import ProjectTable

def index(request):
    template = loader.get_template('core/index.html')

    project_table = ProjectTable(Project.objects.all(), order_by='-code')

    context = {
        'project_table': project_table,
    }
    return HttpResponse(template.render(context, request))