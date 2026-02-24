from django.urls import path
from .views import AddCropView, ListCropsView

urlpatterns = [
    path('add/', AddCropView.as_view(), name='add-crop'),
    path('list/', ListCropsView.as_view(), name='list-crops'),
]