from django.http import HttpResponse
from django.template import loader
from django.views.generic import DetailView

from .models import Project
#from .tables import ProjectTable

def index(request):
    """Index or Dashboard View
    """
    template = loader.get_template('core/index.html')

    projects = Project.objects.all()

    context = {
        'projects': projects,
    }
    return HttpResponse(template.render(context, request))

def project_index(request):
    """Project Index View
    """
    template = loader.get_template('core/project_index.html')
    projects = Project.objects.all()

    context = {
        'projects': projects,
    }
    return HttpResponse(template.render(context, request))


class ProjectView(DetailView):
    """Project Detail View
    """
    model = Project
