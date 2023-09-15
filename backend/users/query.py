from users.models import *
from django.db.models.query import QuerySet


def get_users() -> QuerySet:
    return User.objects.all()


def add_user(name: str, age: int, address: str) -> User:
    return User.objects.create(name=name, age=age, address=address, points=0)


def delete_user(id: int) -> User:
    return User.objects.get(id=id).delete()


def get_user_points(id: int) -> int:
    return User.objects.get(id=id).points


def update_user_points(id: int, points: int) -> User:
    user = User.objects.get(id=id)
    user.points = points
    user.save()
    return user
