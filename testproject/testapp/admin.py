from django.contrib import admin

# Register your models here.
from .models import HttpCall, Parameter

admin.site.register([HttpCall, Parameter])
#Admin account is:
#username: admin
#mail: admin@admin.admin
#pw: admin