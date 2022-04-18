from django.urls import path, include
from .views import get_post

urlpatterns = [
    path('dxarid/',get_post)
]
