from django.urls import path
from . import views

urlpatterns = [
    path(r'',views.reg),
    path(r'auth/',views.authoriz),
    path(r'reg/',views.reg),
    path(r'main/',views.main),
    path(r'write/',views.writing),
    path(r'jour/',views.read_jour)
]