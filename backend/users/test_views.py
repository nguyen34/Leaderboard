from django.test import TestCase, Client
from .views import *
from .models import User
from django.urls import reverse
import json


class UserViewsTestCase(TestCase):
    def setUp(self):
        # Clear out user database before each test
        self.client = Client()
        User.objects.all().delete()

    def test_fetch_users(self):
        # Test that fetch_users returns an empty list when there are no users
        response = self.client.get(reverse('fetch_users'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

        # Test that fetch_users returns a list of all users when there are users
        User.objects.create(name="testuser", age=20,
                            address="testaddress", points=0)
        User.objects.create(name="testuser2", age=20,
                            address="testaddress", points=0)
        response = self.client.get(reverse('fetch_users'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_add_user(self):
        data = {'name': 'testuser', 'age': 20, 'address': 'testaddress'}
        # Test that add_user adds a user to the database
        response = self.client.post(reverse('add_user'), data=json.dumps(data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(User.objects.all()), 1)
        user = response.json()
        self.assertEqual(user['name'], 'testuser')
        self.assertEqual(user['age'], 20)
        self.assertEqual(user['address'], 'testaddress')
        self.assertEqual(user['points'], 0)

    def test_add_user_invalid(self):
        invalid_data = {'name': 'testuser', 'age': 20}
        # Test that add_user returns an error when a field is missing
        response = self.client.post(reverse('add_user'), data=json.dumps(invalid_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message': 'Invalid form data!'})

        # Test that add_user returns an error when a field is empty
        invalid_data = {'name': 'testuser', 'age': 20, 'address': ''}
        response = self.client.post(reverse('add_user'), data=json.dumps(invalid_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message': 'Invalid form data!'})

        # Test that add_user returns an error when a field is invalid
        invalid_data = {'name': 'testuser',
                        'age': '20A', 'address': 'testaddress'}
        response = self.client.post(reverse('add_user'), data=json.dumps(invalid_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message': 'Invalid form data!'})

        # Test that add_user returns an error when age is less than 0
        invalid_data = {'name': 'testuser',
                        'age': -1, 'address': 'testaddress'}
        response = self.client.post(reverse('add_user'), data=json.dumps(invalid_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message': 'Invalid form data!'})

        # Test that add_user returns an error when age is greater than 100
        invalid_data = {'name': 'testuser',
                        'age': 101, 'address': 'testaddress'}
        response = self.client.post(reverse('add_user'), data=json.dumps(invalid_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message': 'Invalid form data!'})

    def test_increment_user_score(self):
        # Test that increment_user_score increments the user's score
        user = User.objects.create(name="testuser", age=20,
                                   address="testaddress", points=0)
        response = self.client.post(
            reverse('increment_user_score', args=[user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.get(id=user.id).points, 1)

    def test_decrement_user_score(self):
        # Test that decrement_user_score decrements the user's score
        user = User.objects.create(name="testuser", age=20,
                                   address="testaddress", points=5)
        response = self.client.post(
            reverse('decrement_user_score', args=[user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.get(id=user.id).points, 4)

        # Test that decrement_user_score does not decrement the user's score below 0
        new_user = User.objects.create(
            name="testuser2", age=20, address="testaddress", points=0)
        response = self.client.post(
            reverse('decrement_user_score', args=[new_user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.get(id=new_user.id).points, 0)

    def test_delete_user(self):
        # Test that delete_user deletes a user from the database
        user = User.objects.create(name="testuser", age=20,
                                   address="testaddress", points=0)
        self.assertEqual(len(User.objects.all()), 1)
        response = self.client.delete(
            reverse('delete_user', args=[user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(User.objects.all()), 0)
