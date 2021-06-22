from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'auth/', views.authoriz),
    re_path(r'reg/', views.reg),
    re_path(r'main/', views.main),
    re_path(r'write/', views.writing),
    re_path(r'jour/', views.read_jour),
    path('', views.reg)
]