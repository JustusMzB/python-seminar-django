from django.urls import path
from testapp.views import hello_world

urlpatterns = [
    path('helloworld/', hello_world, name = 'helloworld'),
]
