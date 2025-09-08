from django.urls import path, include
from .views import (
    CouplingsListView,
    CouplingDetailView,
)

app_name = 'couplings'

urlpatterns = [
    path('', CouplingsListView.as_view(), name='index'),
    path('<int:pk>/', CouplingDetailView.as_view(), name='detail'),
]