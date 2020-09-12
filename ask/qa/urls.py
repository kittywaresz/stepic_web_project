from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.index, name='login'),
    path('signup/', views.index, name='signup'),
    path('questions/<int:id>/', views.index, name='questions'),
    path('ask/', views.index, name='ask'),
    path('popular/', views.index, name='popular'),
    path('new/', views.index, name='new')
]
