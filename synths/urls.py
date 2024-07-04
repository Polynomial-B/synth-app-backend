from django.urls import path
from .views import SynthListView, SynthDetailView

urlpatterns = [
  path('', SynthListView.as_view()),
  path('<int:pk>/', SynthDetailView.as_view())
]
