from django.urls import path
from .views import InspectionListView, InspectionView, InspectionCreate, InspectionUpdate, InspectionDelete


urlpatterns = [
    path('', InspectionListView.as_view(), name='inspection_list'),
    path('create/', InspectionCreate.as_view(), name='inspection_create'),
]