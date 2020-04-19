from django.forms import ModelForm
from .models import Task


class TaskCreateForm(ModelForm):
    """Task Form
    """
    class Meta:
        model = Task
        fields = ['name','description','status']