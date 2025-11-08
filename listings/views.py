from django.shortcuts import render
# listings/views.py
from django.http import JsonResponse

def hello_api(request):
    return JsonResponse({"message": "Welcome to ALX Travel API!"})

# Create your views here.
