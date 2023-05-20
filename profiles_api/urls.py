from django.urls import path
# from profiles_api import views    #we can use this or the one below
from . import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
]