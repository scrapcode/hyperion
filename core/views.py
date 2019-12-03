from django.http import HttpResponse
from django.template import loader
from django.views.generic import DetailView

from .models import Project
from .tables import ProjectTable

def index(request):
    template = loader.get_template('core/index.html')

    projects = Project.objects.all()

    context = {
        'projects': projects,
    }
    return HttpResponse(template.render(context, request))


class ProjectView(DetailView):
    model = Project