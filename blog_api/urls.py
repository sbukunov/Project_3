
from django.urls import path

from . import views

urlpatterns = [
    path('notes/', views.NoteListCreateAPIView.as_view()),
    path('notes/<int:pk>', views.NoteDetailAPIView.as_view()),
]
