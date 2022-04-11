from django.contrib import admin

# Register your models here.
from dxarid.models import *
from dxarid.views import DxaridAPIView

admin.site.register(Main)
admin.site.register(Products)