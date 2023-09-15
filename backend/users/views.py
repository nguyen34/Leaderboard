from django.shortcuts import render
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.csrf import ensure_csrf_cookie
import users.query as query
import json

# Create your views here.


# Fetches all users from the database. Also appends csrf token to the response which we will need for later queries
@ensure_csrf_cookie
def fetch_users(request: WSGIRequest) -> JsonResponse:
    users = list(query.get_users())
    users = [user.to_dict() for user in users]
    return JsonResponse(data=users, safe=False)

# Adds a new User to the leaderboard, starting them off with 0 points
# TODO: Add form validation


def add_user(request: WSGIRequest) -> JsonResponse:
    body = json.loads(request.body)
    name, age, address = body['name'], body['age'], body['address']
    user = query.add_user(name, age, address).to_dict()
    return JsonResponse(data=user, safe=False)

# TODO: Consider combining increment and decrement into one function


def increment_user_score(request: WSGIRequest, id: int) -> JsonResponse:
    points = query.get_user_points(id) + 1
    query.update_user_points(id, points)
    return JsonResponse({"message": f'User ID: {id} score incremented!'})


def decrement_user_score(request: WSGIRequest, id: int) -> JsonResponse:
    points = query.get_user_points(id) - 1
    if points < 0:
        points = 0
    query.update_user_points(id, points)
    return JsonResponse({"message": f'User ID: {id} score decremented!'})

# Deletes a user by a given ID.


def delete_user(request: WSGIRequest, id: int) -> JsonResponse:
    query.delete_user(id)
    return JsonResponse({"message": f'User ID: {id} deleted!'})
