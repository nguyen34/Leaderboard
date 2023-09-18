from django.test import TestCase
from .models import User


class UserModelsTestCase(TestCase):
    def setUp(self):
        # Clear out user database before each test
        User.objects.all().delete()

    def test_user(self):
        User.objects.create(name="testuser", age=20,
                            address="testaddress", points=0)
        user = User.objects.get(name="testuser")
        self.assertEqual(user.name, "testuser")
        self.assertEqual(user.age, 20)
        self.assertEqual(user.address, "testaddress")
        self.assertEqual(user.points, 0)

    def test_user_str(self):
        user = User.objects.create(name="testuser", age=20,
                                   address="testaddress", points=0)
        self.assertEqual(str(user), "testuser")
