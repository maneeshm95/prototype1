from django.urls import path
from . import views

urlpatterns = [
    path('allpateints/', views.getAllPatients, name='patients'),
]
