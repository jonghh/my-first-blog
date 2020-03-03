from django.urls import path
from . import views

urlpatterns = [
    path('cal/', views.calculate, name='calculate'),
]
