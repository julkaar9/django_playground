
(Optional)
### 1. Download and install (You might need to add conda in env variables) anaconda or miniconda  
https://www.anaconda.com/, https://docs.conda.io/en/latest/miniconda.html  
we will use conda environments to containerize out projects.  

(Optional)  
### 2. Open cmd or conda shell to create a new env using  
`conda create -n myenv python=3.9`  
Here flag "n" refers to env name, and we will be using python 3.9  

### 3. Use your favourite IDE, preferably VS Code or Pycharm.  
We will be using VS Code.  
Create a new project dir and open it using vs code.  
(Optional)  
Install the official python (from microsoft) extension for vscode.  
This will help detecting conda envs and much more.

### 4. We will need to install the following python packages
(a) Django - The python based web framework we will use for setting up the backend.  
Install using `conda install -c anaconda django`  
(b) Django rest_framework - This package wil be used for serializing django database model instances into   json and vice versa.  
`conda install -c conda-forge djangorestframework`  

### 5. Once the installation is successfull, create a new django project using.
`django-admin startproject project_name`

django-admin command is used for creating new django projects and fetching project meta-data, such as security state, etc.  
https://docs.djangoproject.com/en/4.1/ref/django-admin/  

Once the project is created cd into the project dir.  
Alternatively you can directly open the new project folder using vscode.  

run `python manage.py runserver` to boot up the django debug server.  

Here manage.py is basically the handler script for django's cli,  
generally used for booting local servers,data migrations, etc.  

If the installation is successful, a server should run on http://127.0.0.1:8000/  

### 6. Django's OOP base DBMS  

Django uses an OOP based database system where classes are used as sql table blueprints.  
The actual sql tables are created using these two commands, which maps python code to sql  
`python manage.py makemigrations` (This command creates intermediate python  
code for the migration, which can be viewed inside migration folders)  
`python manage.py migrate` (This command performs the actual migration)  

The general class based sql approach  
```py
class Table_name(models.Model): # inherits django's Model clas
    field_name = models.FieldType(parms such as default value, max_length, etc)
```

### 7. Django provides a basic authentication system, that we can use to access admin panel.
The necessary model classes are already present, we just need to migrate using the migations commands  

### 8. Create a superuser to access the admin panel.
Run python manage.py createsuperuser and enter your admin details to create the superuser / superadmin.  

You can now visit the admin panel using http://127.0.0.1:8000/admin  

### 9. Django's app system.
Django prefers a low couping module integrations approach. Which revolves around  
segmenting the project into independent sub-projects.  
for instance, the entire authentication system generally never relies too much on the other modules,  
lets say payment gategay.  
So we can separate this two functionalities in two sub-projects or in django term "apps".  

### 10. We will follow this approach and create an app called student, which will contain all student related functionalities.
run- python manage.py startapp student , this will create a student dir.  
Then we need to add this app to our django projects, open `settings.py -> installed_apps` and add "student"   there.

```py
INSTALLED_APPS = [
    ...
    "student",
]
```
### 11. Creating the student models / tables.
Inside the student dir, open models.py.  
Here we will create our student models.  

For the entire explained code refer to  
 https://github.com/julkaar9/django_playground/tree/api/student/models.py  

### 12. Next we will use django rest_framework to create an api on the student database.
First we will need a serializer for converting these data instances into json.  

so create a serializer.py file inside the student dir  

Here again we will use a class based approach to create serializers for your models.  
The class structure follows.  

```py
class modelnameSerializer(serializers.ModelSerializer):

    class Meta:
        model = The model we are going to serialize
        read_only_fields = Name of the read only fields such as primary_key / id
        fields = All the fields we want to serialize and deserialize
```

For the entire explained code refer to  
https://github.com/julkaar9/django_playground/tree/api/student/serializers.py


### 13. Now we need another layer for http requests to interact with these modules, in django term they are called views.

So in the views.py we will create the necessary classes to interact with http methods.  

There are lots of view patterns for different use case,  
the most common being the APIView, which has the following structure.  

```py
class viewName(APIView):
   def http_method_name(self, request):
       here request contains various information about the http request, ie Method, url parms etc.
```

For the entire explained code refer to  
https://github.com/julkaar9/django_playground/tree/api/student/serializers.py

### 14.Finally we need to specify the urls to connect urls with the proper view.

Create a new file named urls.py inside student dir.  
add app_name = "student", so django can find it.  

urls.py should have the following structure  

```py
urlpatterns = [
    path("url_name/", ViewName.as_view(), name="url_name to access it from other views or models"), 
]
```
Now we also need to add the app specific urls to the main project.  

Open project_name -> urls.py and add `path("app_name/", include("app.urls", namespace="app_name"))` to urlpatterns.

All the urls under this app will be availabe at domain_name.com/app_name/* , you can change the app_name to something else also.

For the entire explained code refer to https://github.com/julkaar9/django_playground/tree/api/student/views.py


Thats pretty much it for creating apis using django rest framework.

If you need to interact with the database from admin panel  
Open/ Create admin.py in student dir. Import the model and register it using.  
`admin.site.register(Modelname)`