from django.shortcuts import render
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.
def test_endpoint(request: WSGIRequest) -> JsonResponse:
    return JsonResponse({"message": "Hello World!"})