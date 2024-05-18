from django.urls import path

from . import views

urlpatterns = [
    path('folders/', views.FoldersView.as_view()),
    path('folders/<int:folder_id>', views.FoldersViewId.as_view()),
    path('places/', views.PlacesView.as_view()),
    path('places/<int:id>', views.PlacesViewID.as_view()),
]
