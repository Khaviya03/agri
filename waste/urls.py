from django.urls import path
from .views import AddWasteView, ListWasteView

urlpatterns = [
    path('add/', AddWasteView.as_view(), name='add-waste'),
    path('list/', ListWasteView.as_view(), name='list-waste'),
]