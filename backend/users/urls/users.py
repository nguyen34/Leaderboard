from django.urls import path
import users.views as views

urlpatterns = [
    path("users/fetch/", views.fetch_users, name="fetch_users"),
    path("users/add/", views.add_user, name="add_user"),
    path("users/increment/<int:id>", views.increment_user_score,
         name="increment_user_score"),
    path("users/decrement/<int:id>", views.decrement_user_score,
         name="decrement_user_score"),
    path("users/delete/<int:id>", views.delete_user, name="delete_user"),
]
