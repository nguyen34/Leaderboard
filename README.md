# Spring Financial Full Stack Assessment - Leaderboard

This README provided should help explain certain aspects of my submission for Spring Financial's Full Stack Assessment, which includes how to set up, run as well as explaining some creative liberties I took when designing this project.

This project was developed using VSCode on WSL.

Set up and running the project are seperated between frontend and backend, as detailed below:

# Frontend

The Frontend uses a tech stack of Vue, and Vuex with Jest for testing. Also, coupled into this tech stack is Axios for making API calls and Vuetify for additional components and styling.

(The following steps written below are under the assumption you are in the project's /frontend directory)

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### To run all the frontend tests

```sh
npm run test
```

### Alternatively, you can also run the commands at the root with the provided shell script:

```sh
./sf.sh f run # Equivalent of npm run dev
./sf.sh f test # Equivalent of npm run test
```

Once the project is up and running, you can navigate to the Local url to see the project:

```sh
http://localhost:5173/ # the default
```

# Backend

The backend uses a tech stack of Python and Django. The Database used remains to be SQLite so that this project can be run minimally with little setup for evaluation.

(The following steps written below are under the assumption you are in the project's /backend directory)

## Project Setup

### Activate the virtual environment

```sh
source .env/bin/activate
```

### Install the dependencies:

```sh
pip install -r requirements.txt
```

### Run Migrations (Recommended for first time set up)

```sh
python manage.py migrate # or python3 if you use python3
```

### Compile and run for development

```sh
python manage.py runserver # or python3 if you use python3
```

### To run all the backend tests

```sh
python manage.py test
```

### To open Python interactive shell

```sh
python manage.py shell
```

### Alternatively, you can also run the commands at the root with the provided shell script:

```sh
./sf.sh b run # Equivalent of python manage.py runserver
./sf.sh b test # Equivalent of python manage.py test
./sf.sh b shell # Equivalent of python manage.py shell
```

Assuming it all runs correctly, the developement server should now be running on http://localhost:8000/ where 8000 is the default port.

# Troubleshoot

1. If you're having issues running the shell script due to a permission denied. You can try the following command to enable it:

```sh
chmod u+x sf.sh
```

2. Please also ensure that your node is up to date as well. This project was developed and tested on

```sh
v20.2.0
```

# Assumptions and Creative Liberties

On top of fulfilling the requirements specified in the documentation, I took some assumptions and creative liberties when designing the leaderboards. Namely:

1. I saved user scores into the backend. I do that by making an API call everytime an individual users score is incremented or decremented. I am aware that making an API call so frequently does hamper performance but the scale of this application was small enough that I determine it to not be too much of an issue. if it did impact performance significantly, I would implement an additional button to do a manual save instead. I am aware that this goes against the 'all users start with 0 points' requirement since on subsequent loads, it would load up the user with the last saved points amount it had, but I wanted to have more going on with these points.

2. I restricted the point scoring on the leaderboard so that the user cannot go lower than zero. More of a personal choice since leaderboards I've seen usually don't have negative scores but some can. I just saw it as a good oppurtunity to build a responsive web design to disable the '-' button whenever the user's score was 0.

3. There was no specifications on how adding a user works, so I went with adding an AddNewUserModal to open a separate dialog to handle the creation of a new user. I also added form validation on both the frontend and backend to prevent users from inputting incorrect values (i.e. entering a letter in the age field)

4. There was no specification on how the User Details were to be shoen either, so I also just shown that in a simple dialog. Styling this would be pretty straightforward too so this is easy to adjust if needed.
