from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('projects/<slug>', views.ProjectView.as_view(), name='project_detail'),
]