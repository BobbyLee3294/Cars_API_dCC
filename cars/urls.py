from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars_list),
    path('<int:pk>/', views.car_detail), # these arrows brackets help pass the value through
]