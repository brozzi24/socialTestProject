# socialTestProject
A Django application that includes foundamental functionality of a social media site:
* Login/Logout
* Register 
* view content
* Create content
* Comment on content


## To Run Commands in Container
```bash
$ docker-compose run web ...
```

# Set Up Instructions
1. From the __socialTestProject__ dir run
```bash
$ docker-compose build
```
2. Run the DB migrations
```bash
$ docker-compose run web python manage.py migrate
```
3. Create a superuser for the admin backend
```bash
$ docker-compose run web python manage.py createsuperuser
```
4. Run server. (server will run on localhost port 8000)
```bash
$ docker-compose up
```

