# WebPractDjango
Django Application for movies and series.

## How to run the application

In order to run the application, you must run the command

    `python manage.py runserver`

After that, you have different pages to interact with the application:

    `localhost:8000/admin` --> Admin Interface

    `localhost:8000/FilmRevolutionApp` --> Mainpage of the application

There are some features that are not implemented yet like the details for the
actors, directors, platforms,...

## Requeriments

In the `requeriments.txt` file, you can see the requeriments for the application

## Deployment Schema

* **Application Layer:** FilmRevolution
* **Cookie Storage Layer:** Redis. We will use Redis because of the speed of that NoSQL DataBase.
* **DataBase Layer :** PostgreSQL.We will use PostgreSQL because is multi platform, extensible and have stability and reliability. Also have a good security system by managing users, groups of users and passwords.
* **Reversed Proxy Layer:** NGINX. We will use NGINX because is multi platform, light, high performance, and reverse proxy.
* **Server Layer:** Apache Server with WSGI. We will use Apache Server with WSGI because it's multi platform, extensible and popular. 
