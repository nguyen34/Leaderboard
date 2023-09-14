from django.urls import path
import users.views as views

urlpatterns = [
    path("users/test/", views.test_endpoint),
]
