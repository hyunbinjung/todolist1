from django.urls import path
from .models import *
from .views import TodolistListView, TodolistDetailView,TodolistCreateView, TodolistUpdateView,TodolistDeleteView


urlpatterns = [

    path('',TodolistListView.as_view(),name='list'),
    path('detail/<int:pk>/',TodolistDetailView.as_view(),name='detail'),
    path('create/',TodolistCreateView.as_view(),name='create'),
    path('update/<int:pk>/',TodolistUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',TodolistDeleteView.as_view(),name='delete'),

]
