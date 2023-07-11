# TodoApp
## Initial Set Up
From the command line, navigate to the code directory on the Desktop and create both a todo folder.
```
  # Windows
 > cd onedrive\desktop\code
 > mkdir todo && cd todo

  # macOS
 % cd desktop/desktop/code
 % mkdir todo && cd todo
```
Then run through the standard steps of creating a new virtual environment, activating it, and installing Django.
```
  # Windows
> python -m venv .venv
> .venv\Scripts\Activate.ps1(.venv)
> python -m pip install django

  # macOS
% python3 -m venv .venv
% source .venv/bin/activate(.venv)
% python3 -m pip install django
```
Now that Django is installed we should start by creating a traditional Django project called
django_project, adding an app called todos within it, and then migrating the initial database.
```
(.venv) > django-admin startproject django_project
(.venv) > python manage.py startapp todos
(.venv) > python manage.py migrate
```
Openup django_project/settings.py in your text editor and add todos to the bottom of the installed apps.
## models
we have only two fields: title and body.
Control+c to stop our local server. Then run the ```makemigrations``` command.
And then the ```migrate```command.

Now we can use the built-in Django admin app to interact with our database by explicitly add our Todos app  via the todos/admin.py file

Then we can create a superuser account to log in to the admin
```
(.venv) > python manage.py createsuperuser
```
## add DjangoRESTFramework 
stop the local server by typing Control+c and then install it with Pip

## serializers
Create the serializer which transforms our model data into JSON that will be outputted at our desired URLs.

Create a new file called todos/serializers.py file 
## Views
We will use two DRF generic views here : ListAPIView to display all todos and RetrieveAPIView to display a single model instance.

Next create an app-level todos/urls.pyfile.

## API Tests
Open thetodos/tests.pyfile To test the API

we need to import three new items at the top: reverse from Django,status from Django REST Framework, and APITestCase from Django REST Framework.

Then we add two tests: test_api_listview and test_api_detailview to check both the list and detail pages

use the correct named URL,return 200 status codes, contain only one object, and the response has all the data expected. 





