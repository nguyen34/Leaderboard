from users.urls.users import urlpatterns as users_urls

# This is the list of all the paths in the users app. I seperated them into different files to make it easier to manage and to future proof the app. Kind of a personal preference.
paths = [
    users_urls,
]
