# Django Blog Project

## Step One – Create Project Environment (Using Anaconda)

### 1. Ensure that Anaconda and all of its packages are up to date
- Type `conda update --all -y`

### 2. Install Django as a package in Anaconda
- Type `conda install django -y`

### 3. Create project directory and change into that directory
- Type `mkdir djangoblog cd djangoblog`

4. Create an environment using the command line and install packages
- Type `conda create --name djangoblog python django pandas psycopg3 -y`

5. Activate the environment
- Type `conda activate djangoblog`
---

## Step Two – Create Django Project, Adjust Settings, and Run Dev Server

### 1. Create the Django project
- Type `django-admin startproject djangoblog .`
- The project should now include six Python files inside of the djangoblog directory: "manage.py" sits at the root of the directory, and "__init__.py", "settings.py", "urls.py", "asgi.py", and "wsgi.py" sit inside the subdirectory folder also named djangoblog.

### 2. Adjust initial project settings file
- Open the "settings.py" file in your project directory in your IDE.
- The "settings.py" file is a configuration file for the project website.
- Find the "ALLOWED_HOSTS" line in the file and Type `ALLOWED_HOSTS = ['localhost']`
- Find the "TIME_ZONE" line in the file and fill it in with your Zone.
- Type `TIME_ZONE = 'America/New_York'`
- Find the "LANGUAGE_CODE" line in the file and fill it in as needed.
- Type `LANGUAGE_CODE = en-us`

### 3. Verify the project works by running it in the development server.
- Type `ls` to check if you're at the root of the project directory.
- If at the root, the output will show: "README.md", "djangoblog", and "manage.py" as the two files and one subdirectory inside djangoblog.
- Type `python manage.py runserver` to start the development server.
- Open a browser and Type `127.0.0.1:8000` into the URL.
- If everything is working properly, you will see a Congratulations! page with a rocketship and a message from Django.
---

## Step Three – Create Database and Connect to Blog Application

### 1. Install Database and Set Up User (PostgreSQL)
- Ensure that the "psycopg3" Python module is installed.
- Type `pip install psycopg3` if not already included in initial start-up.
- Download PostgreSQL (figure it out, bud).
- Either download pgAdmin for a GUI client tool to manage the database or use psql in the command line (figure it out, bud).
- Example (Ubuntu and psql): Open a separate tab from the project terminal and Type `sudo apt install postgresql postgresql-contrib` then `sudo -u postgres psql` for the interactive shell.
- To check if psql was installed properly: Type `psql --version` and then `psql` to access the interactive shell.
- Type `sudo systemctl start postgresql.service` to check if PostgreSQL is running, then `sudo systemctl enable postgresql.service` to automatically start PostgreSQL on system boot, and then verify that it is running `sudo systemctl status postgresql.service` by checking its status.
- PostgreSQL automatically creates a default user named "postgres" once it is installed on the system, and the user has full "superadmin" privileges, so this should be changed in order to secure the database.
- Change the password for "postgres" and then choose a strong password and store it in a secure place: Type `sudo passwd postgres` and then enter your information and change into the user account: `sudo su - postgres` in order to modify the PostgreSQL "postgres" user inside psql when it is connecting over a network: `psql -c "ALTER USER postgres WITH PASSWORD 'thisiswherethenewpasswordgoes'"` (this password only applies when "postgres" (user) connects to PostgreSQL over a network, and does not apply locally, since a password is not required for local access).
- Type `psql postgres` to login as "postgres" user.
- Remember: The "postgres" Linux user and the "postgres" database user are different. The Linux account is used to access the database and the PostgreSQL user can perform admin tasks inside the database.
- Enable the "Adminpack" module for management and admin tools: `CREATE EXTENSION adminpack;` then `\dx` to confirm module installation.

### 2. Create and Connect Database to Python Database Module and Django
- While logged in as "postgres" in psql the database will be created.
- Type `create database djangoblog with password [insertpassword];`
- Type `ALTER ROLE djangoblog SET client_encoding TO 'utf8';`
- Type `ALTER ROLE djangoblog SET USE_TZ TO 'America/Chicago';`
- Type `ALTER ROLE djangoblog SET default_transaction_isolation TO 'read committed';`
- Close the psql shell and return to the "settings.py" file and locate the "DATABASES" line in the file.
- Replace the information in the default key values: `DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql_psycopg2','NAME': 'djangoblog','USER':'postgres','PASSWORD': 'password','HOST': 'localhost','PORT': '',}}`
- Find the last line of the file that has "DEFAULT_AUTO_FIELD", start a new line underneath and Type: `import os` and underneath that line: `STATIC_ROOT = os.path.join(BASE_DIR, 'static')`
- Save and close the "settings.py" file.
- Migrate the initial database to our PostgreSQL database in the project environment at the root directory.
- Type `python manage.py makemigrations` to make the database changes.
- Type `python manage.py migrate` to migrate the djangoblog database to Django.
---

### 3. Create Static Folder and Super User Account for Django Project
- Type `python manage.py collectstatic` to "collect" the CSS/HTML/JS folders.
- The static files for the project will be located at the root directory.
- Create an admin superuser for the blog at the project root directory.
- Type `python manage.py createsuperuser` to create an admin account.
- Create the Username for the admin superuser.
- Add the Email address for the admin superuser.
- Enter the Password for the admin superuser twice.
- To access the Admin GUI, the project will need to be running.
- Type `python manage.py runserver`
- Open the web browser and type `localhost:8000`
- Ensure that the site is up and running.
- Type into the URL `localhost:8000/admin` to access the login page.
- Enter the newly create admin superuser account information and hit "Log in"
- If successful, a "Django administration" header should be visible.
---

## Step Four - Create Application and Django Model for Blog
- The Django model is an object that is saved in the database. It will store information about the users, blog posts, dates, etc. The model in the database is similar to a spreadsheet with columns, called "fields" and the rows are the data.
- It is important to keep the project organized, because as a "project" grows, it may need different types of functionality, which would require separate "applications" in order to properly fulfill its duties. One application may be useful in another project, or one project may need multiple applications.
- As a result, it is important to separate the applications used in a project, although they will reside inside the project directory.
- The "djangoblog" root directory is where all of the applications should reside.

### 1. Create Blog Application
- Type `python manage.py startapp blog` to create the main blog application.
- Type `ls` to check the directory to ensure the "blog" directory was created.
- The new blog application should create 6 files: "__init__.py", "admin.py", "apps.py", "models.py", "tests.py", and "views.py" as well as 1 folder called "migrations" in the "blog" directory.
- Open up "settings.py" and navigate to the "INSTALLED_APPS" line and add `'blog',` to the end of the array, and save the file. This tells Django that it should use the Application called "blog" in the project.

### 2. Create A Blog "Post" Model
- Familiarity with the basics of Object-Oriented Programming ("OOP") and the Model-View-Controller ("MVC") architecture is helpful (Figure it out, bud).
- The model of the blog should include: (a) the "Post" object; (b) the "Post" object's properties (post information) - (1) title; (2) author; (3) date of post, and; (4) content; (c) the "Post" object should also include a method called "publish" in order to publish the information.
- Open the "models.py" file in the "blog" directory of the project inside of a code editor and add the following code:
```
# Import files in order to have cross-referencing capabilities
# The "class" keyword is used to define objects - always Uppercase
# The argument passed in the class "models.model" informs Django that the Post model is Django Model and should be saved in our PostgreSQL database.

from django.conf import settings
from django.db import models
from django.utils import timezone

# Create the Post object, its properties, and the publish method
# Properties are defined by their respective "field" or data type: CharField is text with a limited number of characters; TextField is text without a character limit; DateTimeField is explanatory; ForeignKey is how we link certain properties to other models.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content_text = models.TextField()
    date_posted = models.DateTimeField(blank=True, null=True)

    # The "def" keyword is indented in the Object class and is used to create a function or method - always Lowercase.
    # Functions and Methods always return a value, so it is necessary to add a "return" keyword - here a string is being called and returns the Post "title"
    def publish(self):
        self.date_posted = timezone.now()
        self.save()

    def __str__(self):
        return self.title
```

### 3. Add Post Model to Django and Create Model in PostgreSQL

- Go to the Terminal and type `python manage.py makemigrations blog` in order to add the Post model to the project database.
- Type `python manage.py migrate blog` in order to apply the changes to the PostgreSQL database.
- If executed properly, there should be a green "OK" in the output.

### 4. Add Post Model to Django Admin to Add/Edit/Delete Posts

- Open the "admin.py" file in the "blog" directory of the project inside of a code editor and add the following code:
```
# Importing the Post model
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

- Return to the root directory and type `python manage.py runserver` to run the web server and then type in the Admin address `localhost:8000/admin` to access the admin page.
- Log into the admin panel using the credentials created earlier.
- Click on the "+ Add" icon in the Posts section underneath the "BLOG" Header on the admin to create posts.

## Step Five - Create Template, View, and Route for the Blog


### 1. Create a Templates Directory and Template HTML File
- Create a "templates" directory inside of the "blog" directory, and then inside of the "templates" directory, create a file called "blog"
- Create a "posts.html" file inside the "djangoblog/blog/templates/blog" directory.
- Type:
```
<!DOCTYPE html>
<html>
<head>
    <title>Blog Title</title>
</head>
<body>
    <p>Blog Construction in Progress</p>
</body>
</html>
```
- Save the file and quit the development server until Step 3.

### 2. Create the Views for the Blog Application
- Views are where the "logic" of the application is created. In Django, a view is a Python function that receives a web request and returns a web response. The response is usually the contents of a web page, a redirect to another page, an error, or an image, etc. The "view" contains the logic necessary to return the response.
- Essentially, the View bridges the gap between the Model and the Template - the data saved in the database (Model) is displayed in the template (HTML file) through the logic presented in the View.
- Open the djangoblog "views.py" file in the code editor.
- Type:
```
# The "render" function imported allows the creation of the template in views that links the contents of the file to the contents of the "urls.py" file.
from django.shortcuts import render

# Create a function to take the URL request and return the value it receives from the render function that creates the template.
def posts(request):
    return render(request, 'blog/posts.html', {})
```
- Save the file.

### 3. Create the Blog URL Route 
- The "Blog" application inside of the Django project should be the homepage for the entire project. In order to have "localhost:8000" default to the Blog, it needs to be imported from the application files to the project root directory files. This takes place within the "urls.py" file of each directory.
- Open the "urls.py" files from the "djangoblog" directory and create a "urls.py" file in the "blog" directory.
- In the djangoblog "urls.py" file, find the "urlpatterns" array and after the first "path" comma, start a new line underneath it and type `path('', include('blog.urls')),` to direct Django to route the homepage to the blog application.
- Open the blog "urls.py" file and type
```
# Importing the "path" function from Django and the "views" from the blog application
from django.urls import path
from . import views

# Adding the urlpatterns array that is used in the djangoblog "urls.py" file in order to link the two.
# Creating a "posts" view in order to connect it to the root URL of the web page.
# Adding an empty string, plus the name "posts" for the view as an identifier and the URL.
urlpatterns = [
    path('', views.posts, name='posts'),
]
```
- Save the file and type `python manage.py makemigrations`
- Type `python manage.py runserver` and see the results.
- Style the page with CSS and JavaScript and save changes.

### 4. Connect the Model to the Template through Views

- In order to connect the "Posts" view to the "Posts" HTML file, it is necessary to pass the models to the template.
- In our blog "views.py" file we need to add the model in "models.py" in order to make the connection.
- Type `from .models import Post` underneath the first import line for the "render" function. The period before "models" infers that "models.py" is in the same directory as the "views.py" file. The name of the Model is imported.

## Step Six - Connect Django to PostgreSQL to Write/Store/Query Data

### 1. Open the Django Python Shell and Create New Posts
- A QuerySet is a list of objects that relate to a given Model. This allows a user to retrieve data from a database, read the data, filter the data, and manipulate the data in various ways.
- At the root directory, users can access a shell within Django.
- Type `python manage.py shell` and the result will show ">>>" similar to the interactive console in Python. All Python commands may be issued here.
- Import the files necessary to create an object in the database.
- Type `from blog.models import Post`
- Display all post objects: `Post.objects.all()`
- Create an object in PostgreSQL: `Post.objects.create(author=name, title='title_name', content='text')`
- Filter objects: `Post.objects.filter(ex. author=name)`
- Filter (Search): `Post.objects.filter(title__contains='name')` in order to search and filter by a given parameter from the "title" field. Django requires double underscores aka "dunders" to separate field names from operations and titles.
- Publish using "publish" method created earlier: create a variable to assign to the QuerySet method `post = Post.objects.get(title="title_name")` then publish with the "publish" method `post.publish()` and check the result by filtering for the date posted `Post.objects.filter(date_posted___lte=timezone.now())`
- Order objects: `Post.objects.order_by('date_posted')`
- Order objects (Ascending): `Post.objects.order_by('-date_posted')`
- Chain Queries (Complex Queries): `Post.objects.filter(date_posted__lte=timezone.now()).order_by('title')`
- Add more posts the blog through the shell instead of the admin page.

### 2. Add QuerySet to Posts Function in View to Display Posts by Date
- Using the example queries above, the Posts function in blog "Views.py" file should include the QuerySet that filters posts by date posted.
- Open the blog "views.py" file in the code editor.
- Type `from django.utils import timezone` underneath the preceding two import lines in order to have the posts sorted by the actual time they were posted to the blog.
- The QuerySet needs to be added to the function in order to be processed as part of the posts creation methodology before the template is returned.
- Type `post = Post.objects.filter(date_posted__lte-timezone.now()).order_by('date_posted')` in order to add the QuerySet to the function.
- Type `{'post': post}` in the brackets within the render function in order to pass the newly created variable to the template as a parameter.
- The resulting file should look like this:
```
def posts(request):
    post = Post.objects.filter(date_posted__lte-timezone.now()).order_by('date_posted')
    return render(request, 'blog/posts.html', {'post': post})
```
- Save the file and display the QuerySet in the template file.

### 3. Display QuerySet Data within the Template File
- In order to use Python in the Template file, it is necessary to use "template tags," which Django utilizes in order to pass Python-esque commands into HTML for dynamic websites.
- Double curly brackets "{{ }}" are used for template tags.
- Open the "posts.html" file and type `{{ post }}` and save the file.
- Django will render (show) the posts that were created as a list of objects, so in order to display the lists, it is necessary create a "for" loop inside the template tags.
- In order to display each post properly, a mix of HTML and template tags will be necessary.
- Type
```
{% for posts in post %}
    <article>
        <time>Posted On: {{ post.date_posted }}</time>
        <h2><a href="">{{ post.title }}</a></h2>
        <p>{{ post.text|linebreaksbr }}</p>
    </article>
{% endfor %}
```

## Step Seven - 
