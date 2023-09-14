from django.test import TestCase
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest

# Create your tests here.


def test_endpoint(request: WSGIRequest) -> JsonResponse:
    return JsonResponse({"message": "Hello World!"})
