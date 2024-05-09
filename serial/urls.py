# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('serial/', views.serial_list),
    path('serial/<int:pk>/', views.serial_detail),
]
