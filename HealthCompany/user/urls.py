from django.urls import path
from . import views

urlpatterns = [
    path('userregistration/', views.signup_view, name='signup')
]
