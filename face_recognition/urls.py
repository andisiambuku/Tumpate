from django.urls import path
from . import views


urlpatterns = [
    path('face-recognition/', views.face_recognition, name='face-recognition'),
]




