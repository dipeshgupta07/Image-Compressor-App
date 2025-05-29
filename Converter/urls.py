from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This is the key line
    path('process/', views.process, name='process'),
    path('download/', views.download_image, name='download_image'),

]