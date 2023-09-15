from django.shortcuts import render
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.


def test_endpoint(request: WSGIRequest) -> JsonResponse:
    return JsonResponse({"message": "Hello World!"})


@ensure_csrf_cookie
def fetch_users(request: WSGIRequest) -> JsonResponse:
    return JsonResponse({"message": "Users Fetched!"})


def add_user(request: WSGIRequest) -> JsonResponse:
    print(request.body)
    return JsonResponse({"message": "User Added!"})


def increment_user_score(request: WSGIRequest, id: int) -> JsonResponse:
    return JsonResponse({"message": f'User ID: {id} score incremented!'})


def decrement_user_score(request: WSGIRequest, id: int) -> JsonResponse:
    return JsonResponse({"message": f'User ID: {id} score decremented!'})


def delete_user(request: WSGIRequest, id: int) -> JsonResponse:
    return JsonResponse({"message": f'User ID: {id} deleted!'})
