from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('projects/<int:pk>', views.ProjectView.as_view(), name='project-detail'),
]