from django.shortcuts import render
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import UserForm
import users.query as query

import json


def fetch_users(request: WSGIRequest) -> JsonResponse:
    # Returns all the users from the database
    # @returns JsonResponse
    try:
        users = list(query.get_users())
        users = [user.to_dict() for user in users]
    except Exception as e:
        return JsonResponse({"message": f'Error: {e}'}, status=400)
    return JsonResponse(data=users, safe=False)


def add_user(request: WSGIRequest) -> JsonResponse:
    # Adds a new user to the database with a starting point of 0
    # @returns JsonResponse
    data = json.loads(request.body)
    form = UserForm(data)
    if not form.is_valid():
        return JsonResponse({"message": "Invalid form data!"}, status=400)
    name, age, address = data['name'], data['age'], data['address']
    try:
        user = query.add_user(name, age, address).to_dict()
    except Exception as e:
        return JsonResponse({"message": f'Error: {e}'}, status=400)
    return JsonResponse(data=user, safe=False, status=200)


def increment_user_score(request: WSGIRequest, id: int) -> JsonResponse:
    # Increments the points of a user by 1
    # @param id: int. The ID of the user to increment the score of
    # @returns JsonResponse
    try:
        query.increment_user_points(id)
    except Exception as e:
        return JsonResponse({"message": f'Error: {e}'}, status=400)
    return JsonResponse({"message": f'User ID: {id} score incremented!'}, status=200)


def decrement_user_score(request: WSGIRequest, id: int) -> JsonResponse:
    # Decrements the points of a user by 1
    # @param id: int. The ID of the user to decrement the score of
    # @returns JsonResponse
    try:
        query.decrement_user_points(id)
    except Exception as e:
        return JsonResponse({"message": f'Error: {e}'}, status=400)
    return JsonResponse({"message": f'User ID: {id} score decremented!'}, status=200)

# Deletes a user by a given ID.


def delete_user(request: WSGIRequest, id: int) -> JsonResponse:
    # Deletes a user from the database
    # @param id: int. The ID of the user to delete
    # @returns JsonResponse
    try:
        query.delete_user(id)
    except Exception as e:
        return JsonResponse({"message": f'Error: {e}'}, status=400)
    return JsonResponse({"message": f'User ID: {id} deleted!'}, status=200)
