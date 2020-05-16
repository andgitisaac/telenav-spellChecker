from django.urls import path

from . import views

urlpatterns = [
    path('init_db/', views.init_db, name='init_db'),
    path('add_query/', views.add_query, name='add_query'),
    path('', views.index, name='index'),
]