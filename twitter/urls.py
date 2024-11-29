from django.urls import path

from . import views

urlpatterns = [
    path('mapp_tree', views.MappTreeView.as_view()),
    path('twitter', views.TwitterView.as_view()),
]