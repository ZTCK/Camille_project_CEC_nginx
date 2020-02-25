from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logcapture/', views.logcapture, name='logcapture'),
    path('debug/', views.debug, name='debug'),
]