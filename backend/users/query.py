from users.models import *
from django.db.models.query import QuerySet


# Query functions
def get_users() -> QuerySet:
    # Returns all the users from the database
    # @returns QuerySet[User]
    return User.objects.all()


def add_user(name: str, age: int, address: str) -> User:
    # Adds a new user to the database with a starting point of 0
    # @param name: str. The name of the user
    # @param age: int. The age of the user
    # @param address: str. The address of the user
    # @returns User
    return User.objects.create(name=name, age=age, address=address, points=0)


def delete_user(id: int) -> None:
    # Deletes a user from the database
    # @param id: int. The ID of the user to delete
    User.objects.get(id=id).delete()


def get_user_points(id: int) -> int:
    # Returns the points of a user
    # @param id: int. The ID of the user to get the points of
    # @returns int. The points of the user
    return User.objects.get(id=id).points


def update_user_points(id: int, points: int) -> User:
    # Updates the points of a user
    # @param id: int. The ID of the user to update the points of
    # @param points: int. The new points of the user
    # @returns User
    user = User.objects.get(id=id)
    user.points = points
    user.save()
    return user


def increment_user_points(id: int) -> User:
    # Increments the points of a user by 1
    # @param id: int. The ID of the user to increment the points of
    # @returns User
    user = User.objects.get(id=id)
    user.points += 1
    user.save()
    return user


def decrement_user_points(id: int) -> User:
    # Decrements the points of a user by 1
    # @param id: int. The ID of the user to decrement the points of
    # @returns User
    user = User.objects.get(id=id)
    if user.points > 0:
        user.points -= 1
        user.save()
    return user
