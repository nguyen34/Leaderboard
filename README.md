# Leaderboard


Fun Leaderboard web application, originally devised for Spring Financial's full stack assessment but it would be a waste to let it all go for nothing. 

This README includes how to set up, run as well as explaining some creative liberties I took when designing this project.

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
