from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.project_index, name='project_index'),
    path('projects/<slug>', views.project_detail, name='project_detail'),
    path('projects/<slug>/task/create', views.project_task_create, name='project_task_create'),
]
