from django.urls import path

from . import views

urlpatterns = [
    path('places/', views.PlacesView.as_view()),
    path('places/<int:id>', views.PlacesViewID.as_view()),
]
