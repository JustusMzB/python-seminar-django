from django.urls import path
from testapp.views import hello_world, hello_name

urlpatterns = [
    path('helloworld/', hello_world, name = 'helloworld'),
    path('helloname/<str:name>/', hello_name, name = 'helloname'),
]
