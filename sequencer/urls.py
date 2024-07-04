from django.urls import path
from .views import SequencerListView, SequencerDetailView

urlpatterns = [
  path('', SequencerListView.as_view()),
  path('<int:pk>/', SequencerDetailView.as_view())
]
