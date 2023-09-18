from django.test import TestCase
from .forms import *


class UserFormsTestCase(TestCase):

    def test_user_form_is_valid(self):
        # Test that user form is valid when all fields are filled in
        form = UserForm(
            data={'name': 'testuser', 'age': 20, 'address': 'testaddress'})
        self.assertTrue(form.is_valid())

    def test_user_form_is_invalid(self):
        # Test that user form is invalid when a field is missing
        form = UserForm(data={'name': 'testuser', 'age': 20})
        self.assertFalse(form.is_valid())

        # Test that user form is invalid when a field is empty
        form = UserForm(data={'name': 'testuser', 'age': 20, 'address': ''})
        self.assertFalse(form.is_valid())

        # Test that user form is invalid when a field is invalid
        form = UserForm(
            data={'name': 'testuser', 'age': '20A', 'address': 'testaddress'})
        self.assertFalse(form.is_valid())

        # Test that user form is invalid when age is less than 0
        form = UserForm(
            data={'name': 'testuser', 'age': -1, 'address': 'testaddress'})
        self.assertFalse(form.is_valid())

        # Test that user form is invalid when age is greater than 100
        form = UserForm(
            data={'name': 'testuser', 'age': 101, 'address': 'testaddress'})
        self.assertFalse(form.is_valid())
