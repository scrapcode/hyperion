import django_tables2 as tables

from .models import Project


# django-table2 docs:
# https://django-tables2.readthedocs.io/en/latest/index.html

class ProjectTable(tables.Table):
    class Meta:
        model = Project
        template_name = 'core/tables.html'
        attrs = {
            'class': 'table table-striped table-sm table-bordered table-hover',
        }
        fields = ("code", "name", "point_of_contact", "status", "updated")