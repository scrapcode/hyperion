from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.forms.models import modelformset_factory
from django.contrib import messages
from django.shortcuts import redirect

from .models import Project, Task
from .forms import TaskCreateForm
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


def project_detail(request, slug):
    """Project Detail View
    """
    template = loader.get_template('core/project_detail.html')
    project = get_object_or_404(Project, code__iexact=slug)

    task_form = TaskCreateForm

    context = {
        'project': project,
        'task_form': task_form,
    }
    return HttpResponse(template.render(context, request))

def project_task_create(request, slug):
    """Project Task Create View
    """
    project = get_object_or_404(Project, code__iexact=slug)

    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.project = project
            task.save()
            messages.success(request, 'Task for "%s" added successfully.' % (project.name))
        else:
            messages.error(request, 'Failed to add task for "%s"' % (project.name))
    
    return redirect(project_detail, slug=slug)

