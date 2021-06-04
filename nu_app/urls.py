from django.urls import path
from nu_app import views

urlpatterns = [
    path('',views.home , name = "Home")
]