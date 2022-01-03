from django import template
from django.http import HttpResponse
from django.template import loader

def hello_world(request):
    return HttpResponse('Hello World')

def hello_name(request, name):
   template = loader.get_template('testapp/helloname.html')
   context = {'name':name}
   return HttpResponse(template.render(context, request))