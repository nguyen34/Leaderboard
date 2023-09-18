from django.test import TestCase
from .query import *


class UserQueryTestCase(TestCase):
    def setUp(self):
        # Clear out user database before each test
        User.objects.all().delete()

    def test_get_users(self):
        # Test that get_users returns an empty list when there are no users
        self.assertEqual(list(get_users()), [])

        # Test that get_users returns a list of all users when there are users
        User.objects.create(name="testuser", age=20,
                            address="testaddress", points=0)
        User.objects.create(name="testuser2", age=20,
                            address="testaddress", points=0)
        self.assertEqual(len(list(get_users())), 2)

    def test_add_user(self):
        # Test that add_user adds a user to the database
        add_user("testuser", 20, "testaddress")
        self.assertEqual(len(list(get_users())), 1)

        # Test that add_user returns the user that was added
        user = add_user("testuser2", 20, "testaddress")
        self.assertEqual(user.name, "testuser2")
        self.assertEqual(user.age, 20)
        self.assertEqual(user.address, "testaddress")
        self.assertEqual(user.points, 0)

    def test_delete_user(self):
        # Test that delete_user deletes a user from the database
        user = add_user("testuser", 20, "testaddress")
        delete_user(user.id)
        self.assertEqual(len(list(get_users())), 0)

    def test_get_user_points(self):
        # Test that get_user_points returns the correct number of points
        user = add_user("testuser", 20, "testaddress")
        self.assertEqual(get_user_points(user.id), 0)

        new_user = User.objects.create(name="testuser2", age=20,
                                       address="testaddress", points=5)

        self.assertEqual(get_user_points(new_user.id), 5)

    def test_update_user_points(self):
        # Test that update_user_points updates the user's points
        user = add_user("testuser", 20, "testaddress")
        update_user_points(user.id, 5)
        self.assertEqual(get_user_points(user.id), 5)
