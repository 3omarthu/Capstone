# Casting API Backend

## URL

https://capstoneprojectforfsdn.herokuapp.com/

## Getting Started

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### Deployment

##### Heroku

1.  Create an account on heroku
2.  Login with CLI
3.  SetUp requirements.txt
4.  Use a Procfile with a command simialr to this "web: gunicorn app:app" where app is the file name of your python app
5.  SetUp envirmonet variables on in the setup.sh file and in the heroku dashboards (under settings).
6.  Create database on heroku using "heroku addons:create heroku-postgresql:hobby-dev --app name_of_your_application"
7.  Use this command "heroku config --app name_of_your_application" to get the URL of your database (dont forget to update the envirmonet variables)
8.  Push your files to git hub and run it click the "deploy" button after connecting heroku app to your github repository.
9.  Your app is running now.

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Roles

- Casting Assistant
  Can view actors and movies
- Casting Director
  All permissions a Casting Assistant has and…
  Add or delete an actor from the database
  Modify actors or movies

- Executive Producer
  All permissions a Casting Director has and…
  Add or delete a movie from the database

### Permissions

- Casting Assistant
  get:actors
  get:movies

- Casting Director
  get:actors
  get:movies
  patch:actors
  patch:movies
  post:actors
  delete:actors

- Executive Producer
  get:actors
  get:movies
  patch:actors
  patch:movies
  post:actors
  post:movies
  delete:actors
  delete:movies

## Testing

To run the tests, run

python test_app.py

## Setting up authentication

### Login link

https://fsndomar.us.auth0.com/authorize?response_type=token
&client_id=RvGhfinFKqlP2YQJ4JNaGPe7RHPdTEms
&redirect_uri=https://www.google.com/
&scope=SCOPE&audience=http://localhost:8080&state=STATE
