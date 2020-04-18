from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.project_index, name='project_index'),
    path('projects/<slug>', views.ProjectView.as_view(), name='project_detail'),
]