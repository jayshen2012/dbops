from django.urls import include, path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('index/', views.index),
    path('register/', views.register),
    path('submitSql/', views.submitSql),
    path('test/', views.test),
    ]