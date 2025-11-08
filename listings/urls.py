# listings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_api, name='hello'),  # root path of this app
]
