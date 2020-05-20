from django.urls import path

from . import views

urlpatterns = [
    path('history/', views.history, name='history'),
    path('add_query/', views.add_query, name='add_query'),
    path('search/', views.search, name='search'),
]