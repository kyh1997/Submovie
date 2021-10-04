from django.urls import path

from todaymovieapp.views import hello_world

app_name = "todaymovieapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]