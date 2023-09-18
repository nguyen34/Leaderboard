from django.shortcuts import render
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import UserForm
import users.query as query

import json

# Create your views here.


# Fetches all users from the database. Also appends csrf token to the response which we will need for later queries
@ensure_csrf_cookie
def fetch_users(request: WSGIRequest) -> JsonResponse:
    try:
        users = list(query.get_users())
        users = [user.to_dict() for user in users]
    except Exception as e:
        return JsonResponse({"message": f'Error: {e}'}, status=400)
    return JsonResponse(data=users, safe=False)

# Adds a new User to the leaderboard, starting them off with 0 points


def add_user(request: WSGIRequest) -> JsonResponse:
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
    try:
        points = query.get_user_points(id) + 1
        query.update_user_points(id, points)
    except Exception as e:
        return JsonResponse({"message": f'Error: {e}'}, status=400)
    return JsonResponse({"message": f'User ID: {id} score incremented!'}, status=200)


def decrement_user_score(request: WSGIRequest, id: int) -> JsonResponse:
    try:
        points = query.get_user_points(id) - 1
        if points < 0:
            points = 0
        query.update_user_points(id, points)
    except Exception as e:
        return JsonResponse({"message": f'Error: {e}'}, status=400)
    return JsonResponse({"message": f'User ID: {id} score decremented!'}, status=200)

# Deletes a user by a given ID.


def delete_user(request: WSGIRequest, id: int) -> JsonResponse:
    try:
        query.delete_user(id)
    except Exception as e:
        return JsonResponse({"message": f'Error: {e}'}, status=400)
    return JsonResponse({"message": f'User ID: {id} deleted!'}, status=200)
