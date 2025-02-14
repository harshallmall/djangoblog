# Django Blog Project
---
## Step One – Create Project Environment (Using Python and )

### 1. Ensure that Anaconda and all of its packages are up to date
- Type `conda update --all -y`

### 2. Install Django as a package in Anaconda
- Type `conda install django -y`

### 3. Create project directory and change into that directory
- Type `mkdir djangoblog cd djangoblog`

### 4. Create an environment using the command line and install packages
- Type `conda create --name djangoblog python django pandas psycopg3 -y`

### 5. Activate the environment
- Type `conda activate djangoblog`
---
## Step Two – Create Django Project, Adjust Settings, and Run Dev Server

### 1. Create the Django Project
- Type `django-admin startproject djangoblog .`
- The project should now include six Python files inside of the djangoblog directory: "manage.py" sits at the root of the directory, and "__init__.py", "settings.py", "urls.py", "asgi.py", and "wsgi.py" sit inside the subdirectory folder also named djangoblog.

### 2. Adjust Project Settings
- Open the "settings.py" file in your project directory in your IDE.
- The "settings.py" file is a configuration file for the project website.
- Find the "ALLOWED_HOSTS" line in the file and Type `ALLOWED_HOSTS = ['localhost']`
- Find the "TIME_ZONE" line in the file and fill it in with your Zone.
- Type `TIME_ZONE = 'America/New_York'`
- Find the "LANGUAGE_CODE" line in the file and fill it in as needed.
- Type `LANGUAGE_CODE = en-us`

### 3. Verify the Project by Running in Development Server
- Type `ls` to check if you're at the root of the project directory.
- If at the root, the output will show: "README.md", "djangoblog", and "manage.py" as the two files and one subdirectory inside djangoblog.
- Type `python manage.py runserver` to start the development server.
- Open a browser and Type `127.0.0.1:8000` into the URL.
- If everything is working properly, you will see a Congratulations! page with a rocketship and a message from Django.
---
## Step Three – Create Database and Connect to Blog Application
### 1. Install Database and Set Up User (PostgreSQL)
- Ensure that the "psycopg2-binary" Python module is installed.
- Type `pip install psycopg2-binary` if not already included in initial start-up.
- Download PostgreSQL (figure it out, bud).
- Either download pgAdmin for a GUI client tool to manage the database or use psql in the command line (figure it out, bud).
- Example (Ubuntu and psql): Open a separate tab from the project terminal and Type `sudo apt install postgresql postgresql-contrib` then `sudo -i -u postgres` and then `psql` for the interactive shell.
- To check if psql was installed properly: Type `psql --version` and then `psql` to access the interactive shell.
- Type `sudo systemctl start postgresql.service` to check if PostgreSQL is running, then `sudo systemctl enable postgresql.service` to automatically start PostgreSQL on system boot, and then verify that it is running `sudo systemctl status postgresql.service` by checking its status.
- PostgreSQL automatically creates a default user named "postgres" once it is installed on the system, and the user has full "superadmin" privileges, so this should be changed in order to secure the database.
- Change the password for "postgres" and then choose a strong password and store it in a secure place: Type `sudo passwd postgres` and then enter your information and change into the user account: `sudo su - postgres` in order to modify the PostgreSQL "postgres" user inside psql when it is connecting over a network: `psql -c "ALTER USER postgres WITH PASSWORD 'thisiswherethenewpasswordgoes'"` (this password only applies when "postgres" (user) connects to PostgreSQL over a network, and does not apply locally, since a password is not required for local access).
- Type `psql postgres` to login as "postgres" user.
- Remember: The "postgres" Linux user and the "postgres" database user are different. The Linux account is used to access the database and the PostgreSQL user can perform admin tasks inside the database.
- Enable the "Adminpack" module for management and admin tools: `CREATE EXTENSION adminpack;` then `\dx` to confirm module installation.

### 2. Create and Connect Database to Python Module and Django
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
- In the djangoblog "urls.py" file, add `, include` to `from django.urls import path` after "path" and then find the "urlpatterns" array. After the first "path" comma, start a new line underneath it and type `path('', include('blog.urls')),` to direct Django to route the homepage to the blog application.
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
- Save the file and type `python manage.py migrate`
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
        <p>{{ post.content_text|linebreaksbr }}</p>
    </article>
{% endfor %}
```
----
## Step Seven - Prettify the Blog with CSS

### 1. Create a Static Folder and CSS Files
- In order to use CSS inside the Blog application, it is necessary to create a "Static" directory within the application, and then inside the directory, it is necessary to create a "blog.css" file. The end result should be "djangoblog/blog/static/blog.css" in the file structure.
### 2. Add Bootstrap to the HTML File to Streamline CSS Design
- Go to the Bootstrap website, find the "<link>" to add Bootstrap, copy the link, and add it inside the "<head>" element of the "posts.html" file.
- Open the "blog.css" file and customize the application.

### 3. Add Django Template Tag to HTML File to Load Static Directory Files
- In order to ensure CSS is added to the blog, it is necessary to connect the "posts.html" file with a Django template tag to load the Static directory file "blog.css" into the application.
- In the "posts.html" file, add the template tag `{% load static %}` to the top of the file before "<!DOCTYPE html>" in order to load the static files before the Bootstrap files.
- Underneath the Bootstrap link, add `<link rel="stylesheet" href="{% static 'css/blog.css' %}">` in order to inform the template tag where the CSS file is located in the application.

### 4. Edit Body and Post Article in HTML File to Change in CSS File
- Inside the "<article>" element of the blog post section, add "class="posts">" so that it looks like `<article class="post">` when completed. This will allow changes to occur to all posts at once inside the CSS file.
- Inside the "blog.css" file, CSS classes are called with "." and the name of the class. It should look like `.posts {}` inside the file.
- Create a container and a class for both the headings in the posts and the content in the posts inside the "posts.html" file with "<div>" elements. It should look like 
```
<main class="container">
    <div class="post titles">
        <div class="posts">
            {% for posts in post %}
                <article class="post">
                    <time>Posted On: {{ post.date_posted }}</time>
                    <h2><a href="">{{ post.title }}</a></h2>
                    <p>{{ post.content_text|linebreaksbr }}</p>
                </article>
            {% endfor %}
        </div>
    </div>
</main>
```        
- Make design choices in the "blog.css" file, save all of the files, and check the site.

## Step Eight - Create and Extend Base to Post Template and Extend the Blog Application

### 1. Create Base Template to Reuse in Application
- When a layout is needed for multiple use-cases, or users would like to have changes made across multiple places, then a base template is necessary to extend to every page of a website.
- Create a "base.html" file in the same directory as "posts.html" which will be "djangoblog/blog/templates/blog/base.html" as the end result.
- In the "base.html" file, copy the contents from the "posts.html" file.
- Then it is necessary to edit the contents in the "<body>" element, so that everything between and including `{% for posts in post %}` & `{% endfor %}` are replaced with `{% block content %} {% endblock %}` only. 
- This action creates a "block" that informs Django that HTML will come from the "posts.html" template that "extends" this template.

### 2. Extend Base Template by Editing Post Template with New Template Tags
- The original template that was used for the Post template is going to be "extended" to be used as the Base template by placing all of the code in the content blocks in order to have the "block" template tag in the Base template match the tag in the "posts.html" file.
- Edit the "posts.html" file and type
```
{% block content %}
    {% for posts in post %}
        <article class="posts">
            <time class="date">
                {{ post.date_posted }}
            </time>
            <h2><a href="">{{ post.title }}</a></h2>
            <p>{{ post.content_text|linebreaksbr }}</p>
        </article>
    {% endfor %}
{% endblock %}
```
- Similar to before, the block content contains everything that will be extended to the "base.html" template.
- In order to connect the two templates, it is necessary to "extend" the "posts.html" template to the "base.html" template.
- At the top of the "posts.html" file, type `{% extends 'blog/base.html' %}` in order to let Django know that the file is meant to connect to the Base Template.
- Save the files, run the server, and check the changes.

### 3. Extend the Blog Application
- In order to isolate a single post, and display the post on its own page, it is necessary to create a route.
- To do this effectively, it is necessary to add a link inside "blog/templates/blog/posts.html" so that the link from the post's title in the list of posts to the individual post's detailed page.
- Reopen "posts.html" and change the `<h2><a href="">{{ post.title }}</a></h2>` line in the file to:
`<h2><a href="{% url 'post_details' pk=post.pk %}">{{ post.title }}</a></h2>`
- This line creates a template tag that creates a URL in "blog/urls.py" for name=post_details, and utilizes the primary key "pk" which is a unique identifier for each database record in a table.
- There was no primary key deisgnation in our Post model, and in Django, each model can have a field that is the primary key, in addition to its actual name, alongside the "pk" as a reference as well.
- In this instance, Django created one (the default, a field named "id" which holds a number that increases with each corresponding database record) and added it to each post. The primary key is accessed when "post.pk" is used similar to other fields in the Post object.
- Once this is saved, and the server is refreshed, there will be an error since there is no URL or View for "post_details"
### 4. Create new URL for Detailed Post Pages
- Open "blog/urls.py" in order to create the URL.
- The URL should route the user to whichever number is tied to the specific post. e.g., "localhost:8000/posts/<int:pk>/" where "<int:pk>" is Django expecting an integer and exchange the integer to a view as a variable called "pk" or primary key as previously mentioned. So, if someone enters "localhost:8000/posts/3/ into the browser, Django will recognize that the user is looking for the view called "post_details" and send the corresponding information of "pk" equals "5" to that particular view.
- Add the line to the "blog/urls.py" file underneath the first path in "urlpatterns" as `path('posts/<int:pk>/', views.post_details, name='post_details'),`
- Once this is saved, there will still be an error, as there is no corresponding View that has been created yet.

### 5. Create View for Detailed Post Pages
- The view will be given the primary key "pk" parameter, and the view must be able to recognize it, so creating a function with the same name in the parameter as the "blog/urls.py" parameter "pk=post.pk" is necessary.
- Using querysets, it will be utilized to get one blog post at a time.
- In "blog/views.py" add the following:
```
from django.shortcuts import render, get_object_or_404

# Add the function to the end of the file for the new View
def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_details.html', {'post': post})
```
- It is important to know that we added "post_details.html" in the function, which should return a template HTML file that structures how detailed posts should look, but it has not been created yet.
- Once it is saved, refreshed, and a post is clicked on, an error will show because the template page has not been created yet.

### 6. Create Template for Detailed Post Pages
- Inside the "blog/templates/blog" directory, create a file called post_details.html and inside the file type the following:
```
{% extends 'blog/base.html' %}

{% block content %}
    <article class="post">
        {% if post.date_posted %}
            <time class="date">
                {{ post.date_posted }}
            </time>
        {% endif %}
        <h2>{{ post.title }}</h2>
        <p>{{ post.content_text|linebreaksbr }}</p>
    </article>
{% endblock %}
```
- As is evident from the code block, the base template is being extended and inside the content block, the post's date, title, and text are published (if any or all exist).
- Furthermore, the template tag includes "{% if ... %} & {% endif %}" which is the Python if/else to check if the "date_posted" is empty or not, and then publishes it if it exists.
- Save the files, refresh the page, and the error should be gone.
- With the project environment up and running type `python manage.py collectstatic` to update the static files.

## Step Nine – Create ModelForm for Post Model to Add/Edit Posts, Link the Form, and Create a New URL, View, and Template
- By creating a ModelForm for the Post Model, it allows adding and editing blog posts occur on the website, aside from the Admin page.
- Within the main "blog" directory, it is necessary to create a "forms.py" file.
- Open the file and add the following code:
```
# Import Django forms
from django import forms
# Import the Post model
from .models import Post

# Name of the ModelForm and tells Django this class is a ModelForm.
class PostForm(forms.ModelForm):
    # Tells Django which Model is to be used to create the form.
    # Tells Django which fields are to be used in the form.
    class Meta:
        model = Post
        fields = ('title', 'content_text',)
```
- At this point, the "date_posted" is in the View that we just created earlier, and the "author" is the user that is currently logged in.
- Save the file and create a new link to the page, a URL, a View, and a Template.

### 1. Create a Link to the Detailed Pages
- First, it is necessary to create a subdirectory to store icons for the project. The file path should be "blog/templates/blog/icons" and all icons files should be saved there.
- Once, the subdirectory is created, navigate to the Bootstrap website, and select an icon that will signify the ability to create and publish a new blog post and the edit blog post.
- For this example, the icon "file-earmark-plus-fill.svg" will be used for new posts, and the icon "pencil-fill.svg" will be used for editing posts, and both will be placed in the icons subdirectory.
- For the new post portion, open "base.html" in the "blog/templates/blog" directory in order to add this icon to the base template. This is the link.
- Type the following line inside the "div" element inside the "header" section, before the (h1) element:
```
<a href="{% url 'new_post' %}" class="top-menu">
    {% include './icons/file-earmark-plus.svg' %}
</a>
```
- The use of the template tag and "include" tells Django to add the button and its content to the base template, and then provides a reference to the new view "new_post" that must be created in order to avoid errors like before. 
- The final edited version of the "base.html" file should look like this:
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp" crossorigin="anonymous">
        <link rel="stylesheet" href="{% static 'css/blog.css' %}">
        <title>Blog</title>
    </head>
    <body>
        <header class="page-header">
          <div class="container">
            <a href="{% url 'new_post' %}" class="top-menu">
                {% include './icons/file-earmark-plus-fill.svg' %}
            </a>
            <h1><a href="/">Blog</a></h1>
          </div>
        </header>
        <main class="content-container">
            <div class="post-titles">
                <div class="post">
                {% block content %}
                {% endblock %}
                </div>
            </div>
        </main>
    </body>
</html>
```
- Save the file and refresh the browser. It will show the "no ReverseMatch" error as expected. The route URL must be created.
- For the edit posts portion, open "blog/templates/blog/post_details.html" and similar to the above, type the following in the HTML article element
```
<aside class="actions">
    <a class="btn btn-primary" href={% url 'edit_posts' pk=post.pk %}">
        {% include './icons/pencil-fill.svg' %}
    </a>
</aside>
```
- The final edited version of the "post_details.html" file should look like this::
```
{% extends 'blog/base.html' %}

{% block content %}
    <article class="post">
        <aside class="actions">
            <a class="btn btn-primary" href={% url 'edit_posts' pk=post.pk %}">
                {% include './icons/pencil-fill.svg' %}
            </a>
        <aside>
        {% if post.published_date %}
            <time class="date">
                {{ post.date_posted }}
            </time>
        {% endif %}
        <h2>{{ post.title }}</h2>
        <p>{{ post.content_text|linebreaksbr }}</p>
    </article>
{% endblock %}
```
- Save the file and refresh the browser. It will show the "no ReverseMatch" error as expected. The route URL must be created.

### 2. Create URLs Route to the New Post and Edit Posts
- For the new post portion, open "blog/urls.py" and add a new line to the existing list to create the new URL route.
- Type `path('post/new/', views.new_post, name='new_post'),` at the end of the list.

- For the edit posts portion, open "blog/urls.py" and add a new line to the existing list to create the "edit posts" URL route.
- Type `path('post/<int:pk>/edit/', views.edit_posts, name='edit_posts'),` at the end of the list.
- The final "urls.py" file should look like this:
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('posts/<int:pk>/', views.post_details, name='post_details'),
    path('post/new/', views.new_post, name='new_post'),
    path('post/<int:pk>/edit/', views.edit_posts, name='edit_posts'),
]
```
- Save the file and refresh the browser. It will show the "AttributeError" as expected. The "new_post" and "edit_posts" Views must be created.
### 3. Create View Functions for New Posts and Editing Posts
- Open "blog/views.py" and add a new import line and a new Post Form function in order to call it to a new template called "edit_posts.html" so that users can add and edit new posts.
- At the beginning of the file, it is practical to include the ability to view the newly created page after posting, so it will be necessary to include the following import to make this possible: `from django.shortcuts import redirect`
- Under the existing functions in the file, type `from .forms import PostForm` to import the "forms.py" file and the PostForm method from Django.
```
# Create a new Function called "new_post" and request that it publishes the new post form, and then calls the function to be passed to the new template called "edit_posts.html" and display the form inside the template.
def new_post(request):
    form = PostForm()
    return render(request, 'blog/edit_posts.html', {'form': form})
```
- When the form is submitted, the same view will be rendered, but it will have data that is being requested to be published "(i.e., edit_posts.html: <form> method='POST')", in request.POST.
- 
- There are two situations with this new View, accessing the new post page with a blank form for the first time, and then going back to the View with the data that has just been entered into the form.
- In order to distinguish between the two, we must add a conditional "if/else" statement. If 'method == "POST"' then then the PostForm is built with the user data, a function is created to check the form for correctness (required fields filled out with no incorrect values), and if it is, then the user may add an author (required and there was intentionally no field in the PostForm), and preserve the changes by saving it.
- The complete function for the new_post View:
```
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_posted = timezone.now()
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/edit_posts.html', {'form': form})
```
- Save the file, and refresh the page. Without the template, there will be an error, as expected. It must be created now.
- For the edit posts portion, it is necessary to add a function to the "blog/views.py" in order to edit posts.
- While it is nearly identical to the new_post function, there are a few key differences, such as two pk parameters from "urls.py" for the "404 error" and another for the "redirect" in post_details, as well as two PostForm instances when the form is created, one for saving the form, and another when a form is opened from a post to be edited.
- The complete function for the edit_post view looks like this:
```
def edit_posts(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_posted = timezone.now()
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_posts.html', {'form': form})
```
- Save the file, and refresh the page. When navigating to the post_details page, there will be an edit button, and when it is clicked upon, the form with the blog post will be rendered.
- It is necessary to create the Template for editing posts.
### 4. Create Templates for Editing Posts
- Create a new file called "edit_posts.html" in the directory "blog/templates/blog" and go to the file.
- The form needs to be displayed, it needs to be contained within an HTML Form element, and a "Save" button is needed for functionality.
- It is also necessary to secure the form against Cross-Site Request Forgery ("CSRF"), which is an attack that forces an end user to execute unwanted actions on a web application in which they're currently authenticated. This exploit allows unauthorized comments to be submitted in a form where the application already trusts the user.
- Type
```
{% extends 'blog/base.html' %}

{% block content %}
    <h2>New Post</h2>
    <form method="POST" class="post-form">{% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="save-button button-primary">Save</button>
    </form>
{% endblock %}
```
## Step Ten – Secure and Deploy the Application

### 1. Add User-Based Conditional For Editing Posts
- In order to prevent non-registered users from creating or adding posts to the website, it is necessary to add template tags with conditional statements to "base.html" and "post-details.html" in order to ensure that the button links for each are not visible unless the user is registered.
- For "base.html" find the "<header>" statement:
```
<header class="page-header">
    <div class="container">
        {% if user.is_authenticated %}
            <a href="{% url 'new_post' %}" class="top-menu">
                {% include './icons/file-earmark-plus-fill.svg' %}
            </a>
        {% endif %}
        <h1><a href="/">Blog</a></h1>
    </div>
</header>
```
- For "post_details.html" find the "<header>" statement:
```
{% if user.is_authenticated %}
     <a class="btn btn-primary" href="{% url 'post_edit' pk=post.pk %}">
        {% include './icons/pencil-fill.svg' %}
     </a>
{% endif %}
```
- Save the files and load the site in a private browser. It will show that the links and icons aren't available.

### 2. Add User Registration and Login/Logout Page, Add a Login Template, Add Decorators to Privileged User Views, Add New Views to Save New Posts as Drafts, Publish Posts, Delete Posts, and Add If/Then Conditionals to Base Template with Buttons, and the Ability to Log Out
- Django has plenty of authentication tools as a part of its "batteries included" framework, so rather than invent the wheel, it is practicable to use those tools.
- First, open "djangoblog/urls.py" and add URL routes for the login, logout, drafts, publish, and delete pages.
- Type `path('accounts/login/', views.LoginView.as_view(), name='login'),` for the login, `path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),` for the logout, `path('drafts/', views.draft_posts, name='draft_posts'),` for drafts, `path('post/<pk>/publish/', views.publish_posts, name='publish_posts'),` for the publish, and `path('post/<pk>/delete/', views.delete_posts, name='delete_posts')` for the delete URL.
- The completed "djangoblog/urls.py" file should look like this:
```
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('drafts/', views.draft_posts, name='draft_posts'),
    path('post/<pk>/publish/', views.publish_posts, name='publish_posts'),
    path('post/<pk>/delete/', views.delete_posts, name='delete_posts')
]
```
- The login View will send the user to the home page, and the logout View will send the user to the logout page. It is necessary to create the others.
- First, in order to save the posts as drafts, it is necessary to remove the "date_posted" lines in the new_post and edit_posts functions rather than have them be immediately published. Remove `post.date_posted = timezone.now()` from each function or simply add a comment sign in from of them.
- Similar to the queryset that was created when the "Posts" View was made, the same steps will be used when creating the "Drafts" View.
- Add another line in the 'blog/templates/blog/base.html" so that drafts are only visible to authenticated users. Make sure the line is in the "{% if user.is_authenticated %}" template tag block.
- Type `<a href="<div data-gb-custom-block data-tag="url" data-0='draft_posts'></div>" class="top-menu"><span class="glyphicon glyphicon-edit"></span></a>` and save the file.
- Open "blog/views.py" and type the corresponding "Drafts" View function:
```
def draft_posts(request):
    # The queryset ensures that only posts without published dates are gathered and ordered by their created dates.
    posts = Post.objects.filter(date_posted__isnull=True).order_by('date_created')
    return render(request, 'blog/draft_posts.html', {'posts': posts})
```
- After the View is created, it is necessary to create a corresponding template. Create a file draft_posts.html in the directory tree "blog/templates/blog" and type the following:
```
{% extends 'blog/base.html' %}

{% block content %}
    {% for post in posts %}
        <article class="post">
            <time class="date">
                {{ post.date_created }}
            </time>
            <h2><a href="{% url 'post_details' pk=post.pk %}">{{ post.title }}</a></h2>
            <p>{{ post.content_text|truncatechars:200 }}</p>
        </article>
    {% endfor %}
{% endblock %}
```
- Add a button to "post_details.html" that will publish the posts.
- Open the file and edit the lines starting at "{% if post.date_posted %}" and the final result should look like this:
```
{% if post.date_posted %}
    <time class="date">
        {{ post.date_posted }}
    </time>
{% else %}
    <a class="btn btn-primary" href="{% url 'publish_posts' pk=post.pk %}">Publish</a>
{% endif %}
```
- The if/then condition means that if there is no date posted then it gets sent to drafts and a date created is affixed to the post. Save the file.
- Next, create a "publish_post" function in "blog/views.py" as the "Publish" View:
```
def publish_posts(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # This method references the function that was previously created in the Post Model.
    post.publish()
    return redirect('post_details', pk=pk)
```
- Add a "Delete" post line to the "post.details" template underneath the "edit" portion, and then create the "Delete" View.
- Type undeneath the "edit_posts" portion:
```
<a class="btn btn-primary" href="{% url 'delete_posts' pk=post.pk %}">
    {% include './icons/trash-fill.svg' %}
</a>
```
- Finally, add the "delete_posts" function as the "Delete" View in "blog/views.py" for the final step.
- The "post_details.html" file should look like this when it is finished:
```
{% extends 'blog/base.html' %}

{% block content %}
    <article class="post">
        <aside class="actions">
            <a class="btn btn-primary" href="{% url 'publish_posts' pk=post.pk %}">
                Publish
            </a>
            <a class="btn btn-primary" href="{% url 'edit_posts' pk=post.pk %}">
                {% include './icons/pencil-fill.svg' %}
            </a>
        <aside>
        {% if post.date_posted %}
            <time class="date">
                {{ post.date_posted }}
            </time>
        {% else %}
            <a class="btn btn-primary" href="{% url 'delete_posts' pk=post.pk %}">
                {% include './icons/trash-fill.svg' %}
            </a>
        {% endif %}
        <h2>{{ post.title }}</h2>
        <p>{{ post.content_text|linebreaksbr }}</p>
    </article>
{% endblock %}
```
- Second, it is necessary to use the Django "decorators" in order to add the authentication. On the line above each View function, type `@login_required` in order to make them require an account login to utilize.
- Save the file and refresh the page.
- Third, create a template for the login page with the directory name "registration" in "blogs/templates/registration" and create a file inside called "login.html."
- The "login.html" file should look like this:
```
{% extends "blog/base.html" %}

{% block content %}
    {% if form.errors %}
        <p>Username and Password did not match. Please try again.</p>
    {% endif %}
    <form method="post" action="{% url 'login' %}">
    {% csrf_token %}
        <table>
        <tr>
            <td>{{ form.username.label_tag }}</td>
            <td>{{ form.username }}</td>
        </tr>
        <tr>
            <td>{{ form.password.label_tag }}</td>
            <td>{{ form.password }}</td>
        </tr>
        </table>
        <input type="submit" value="login" />
        <input type="hidden" name="next" value="{{ next }}" />
    </form>
{% endblock %}
```
- In order to redirect from the login page to the home page, it is necessary to add in "djangoblog/settings.py" file. Open the "settings.py" file, and add type `LOGIN_REDIRECT_URL = '/'` and save the files.
- Finally, it is practical to add a login button to "blog/templates/blog/base.html" file so that a login button appears to non-privileged users on the website. It is also functional to add details to show users when they are logged in, and add a link to log out, since Django already handles logging in.
- In the file, type in the "<header>" element and between the <body> element:
```
<body>
    <div class="page-header">
        {% if user.is_authenticated %}
            <a href="{% url 'new_post' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
            <a href="{% url 'post_draft_list' %}" class="top-menu"><span class="glyphicon glyphicon-edit"></span></a>
        {% else %}
            <a href="{% url 'login' %}" class="top-menu"><span class="glyphicon glyphicon-lock"></span></a>
        {% endif %}
        <h1><a href="/">Django Girls Blog</a></h1>
    </div>
    <div class="content container">
        <div class="row">
            <div class="col-md-8">
            {% block content %}
            {% endblock %}
            </div>
        </div>
    </div>
</body>
```

### 3. Create a Model for Comments, Add Comments to Database, Add Comment Model to Admin Page, Commit the Application to GitHub, and Deploy the Application to a Virtual Private Server
- In order to allow for feedback on Posts, it is necessary to create a new Class in the Post Model to allow for readers to view comments, but only post them if they are logged into the website.
- Open "blog/models.py" and create the "Comment" Class and necessary functions.
- Type:
```
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    approval = models.BooleanField(default=False)

    def approve(self):
        self.approval = True
        self.save()

    def __str__(self):
        return self.text
```
- Save the file.
- The next step is to allow the Comment section be seen on pages with detailed posts. Open the "post_details.html" file and add lines before the "{% endblock %}" tag:
```
{% for comment in post.comments.all %}
    <div class="comment">
        <div class="date">{{ comment.date_created }}</div>
        <strong>{{ comment.author }}</strong>
        <p>{{ comment.content_text|linebreaks }}</p>
    </div>
{% empty %}
    <p>No Comments</p>
{% endfor %}
```
- It is necessary to allow the ability to add comments on the blog. This requires a CommentForm. Open "blog/forms.py" and create a CommentForm at the end of the file. First, import the Comment Model, so that it looks like `from .models import Post, Comment` and then type:
```
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content_text',)
```
- Then, it is necessary to include the "Add Comment" to the Detailed Posts page in "blog/post_details.html" for the ability to add comments to posts.
- Type `<a class="btn btn-default" href="{% url 'post_comments' pk=post.pk %}">Add Comment</a>` and the final result of the template should look like this:
```
{% extends 'blog/base.html' %}

{% block content %}
    <article class="post">
        <aside class="actions">
            <a class="btn btn-primary" href="{% url 'edit_posts' pk=post.pk %}">
                {% include './icons/pencil-fill.svg' %}
            </a>
            <a class="btn btn-primary" href="{% url 'delete_posts' pk=post.pk %}">
                {% include './icons/trash-fill.svg' %}
            </a>
        <aside>
        {% if post.date_posted %}
            <time class="date">
                {{ post.date_posted }}
            </time>
        {% else %}
            <a class="btn btn-primary" href="{% url 'publish_posts' pk=post.pk %}">
                Publish
            </a>
        {% endif %}
        <h2>{{ post.title }}</h2>
        <p>{{ post.content_text|linebreaksbr }}</p>
        <hr>
        <a class="btn btn-default" href="{% url 'post_comments' pk=post.pk %}">
            Add Comment
        </a>
        {% for comment in post.comments.all %}
            <div class="comment">
                <div class="date">{{ comment.date_created }}</div>
                <p>{{ comment.author }}</p>
                <p>{{ comment.content_text|linebreaks }}</p>
            </div>
        {% empty %}
            <p>No Comments</p>
        {% endfor %}
    </article>
{% endblock %}
```
- In order to avoid the "NoReverseMatch" that was previously seen before, it will be necessary to open "blog/urls.py" and create a new URL to route to a new page for adding comments.
- At the end of "urlpatterns," type the pattern `path('post/<int:pk>/comment/', views.post_comments, name='post_comments'),` and save the file.
- As seen before, the "AttributeError" will occur unless the corresponding View "post_comments" and template "post_comments.html" are also created. 
- First, import CommentForm, and open "blog/views.py" and type:
```

def post_comments(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_comments.html', {'form': form})
```
- Second, create a new file in "blog/templates/blog" called "post_comments.html" and type:
```
{% extends 'blog/base.html' %}

{% block content %}
    <h1>New Comment</h1>
    <form method="POST" class="post-form">{% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary">Post</button>
    </form>
{% endblock %}
```
- Next, we want to display the comments on the "Posts" page, so we can open "blog/posts.html" and type `<a href="{% url 'post_details' pk=post.pk %}">Comments - {{ post.comments.count }}</a>` underneath "{{ post.content_text }}" and the final result of the template should look like this:
```
{% extends 'blog/base.html' %}

{% block content %}
    {% for post in posts %}
        <div class="post">
            <div class="date">
                {{ post.date_posted }}
            </div>
            <h1><a href="{% url 'post_details' pk=post.pk %}">{{ post.title }}</a></h1>
            <p>{{ post.content_text|linebreaksbr }}</p>
            <a href="{% url 'post_details' pk=post.pk %}">Comments - {{ post.comments.count }}</a>
        </div>
    {% endfor %}
{% endblock content %}
```
- In order to limit comments that are visible and moderate them, there will be an added capability to approve or delete comments. This requires: adding to "post_details.html"; appending two URL routes called "delete_comments" and "approve_comments"; editing "posts.html" to show only approved comments, and; adding "approve_comments" method to the Post Model.
- First, open "post_details.html" and change the "{% for comment...% }" block to the following:
```
{% for comment in post.comments.all %}
    {% if user.is_authenticated or comment.approve_comments %}
    <div class="comment">
        <div class="date">
            {{ comment.date_created }}
            {% if not comment.approve_comments %}
                <a class="btn btn-primary" href="{% url 'delete_comments' pk=comment.pk %}"><button type="submit" class="btn btn-primary">
                    Delete Comment
                    </button>
                </a>
                <a class="btn btn-primary" href="{% url 'approve_comments' pk=comment.pk %}"><button type="submit" class="btn btn-primary">
                    Approve Comment
                    </button>
                </a>
            {% endif %}
        </div>
        <p>{{ comment.author }}</p>
        <p>{{ comment.content_text|linebreaks }}</p>
    </div>
    {% endif %}
{% empty %}
    <p>No Comments</p>
{% endfor %}
```
- To get rid of the inevitable "NoReverseError" the two URL route patterns must be added to "blog/urls.py" for each comment decision.
- Open the file and type `path('comment/<int:pk>/approve/', views.approve_comments, name='approve_comments'),` and `path('comment/<int:pk>/delete/', views.delete_comments, name='delete_comments'),` to the end of the "urlpatterns" list.
- To get rid of the inevitable "AttributeError" the two Comment Views must be created in "blog/views.py"
- Open the file and import the Comment at the top of the file to look like: `from .models import Post, Comment` and then type the two following functions with the appropriate login decorators:
```
@login_required
def approve_comments(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_details', pk=comment.post.pk)

@login_required
def delete_comments(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_details', pk=comment.post.pk)
```
- Open "posts.html" and change the line `# <a href="{% url 'post_details' pk=post.pk %}">Comments - {{ post.comments.count }}` to `<a href="{% url 'post_details' pk=post.pk %}">Comments - {{ post.approved_comments.count }}</a>` in order to view the number of "approved" comments.
- Finally, open "blog/models.py" to add a new method to the Comment Class in order to have the queryset filter the approved comments, and type:
```
def approve_comments(self):
    return self.comments.filter(approve_comments=True)
```
- In order to add the Comment Model to the database, it is necessary to tell Django that we made changes to "models.py"
- Type `python manage.py makemigrations blog` and hit enter. If successful, there will be an output that says "- Create model comment"
- Type `python manage.py migrate blog` and hit enter. If successful, there will be an output that says "Applying blog.0002_post_date_created_comment... OK"
- In order to access the database in the Admin page, it is necessary to register the Comment Model. Open "blog/admin.py" and add the Comment Model to the imports, so it looks like this: `from .models import Post, Comment` and then add `admin.site.register(Comment)` underneath the "admin.site.register(Post)" line.
- The final version of the "blog/admin.py" file should look like this:
```
from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
```
- Commit to Git and Push the application to GitHub.
- Type `git add .` then `git commit -m 'commit to main'` and then `git push` in order to push the code to GitHub.
- Make sure the site has the proper configurations to ensure that it is secure.
- Utilize "certbot" or "Letsencrypt" to add SSL certificates to the site in order to make it secure via HTTPS.
- Below is a sample NGINX .conf file that will get one at least an 'A' grade on the website with "Qualys SSL Labs":
```
  server {
  listen [::]:80;
  listen      80;
  server_name domain.tld www.domain.tld;

  # Redirect all non-https requests
  rewrite ^ https://$host$request_uri? permanent;
}

server {
  listen [::]:443 ssl http2 default_server;
  listen      443 ssl http2 default_server;

  server_name domain.tld www.domain.tld;

  # Certificate(s) and private key
  ssl_certificate /etc/ssl/domain.crt;
  ssl_certificate_key /etc/ssl/domain.key;

  # RFC-7919 recommended: https://wiki.mozilla.org/Security/Server_Side_TLS#ffdhe4096
  ssl_dhparam /etc/ssl/ffdhe4096.pem;

  # Or, generate random dhparam
  # openssl dhparam 4096 -out /etc/ssl/dhparam.pem
  # ssl_dhparam /etc/ssl/dhparam.pem;

  ssl_protocols TLSv1.3 TLSv1.2;
  ssl_prefer_server_ciphers on;
  ssl_ecdh_curve secp521r1:secp384r1;
  ssl_ciphers EECDH+AESGCM:EECDH+AES256;

  ssl_session_cache shared:TLS:2m;
  ssl_buffer_size 4k;

  # OCSP stapling
  ssl_stapling on;
  ssl_stapling_verify on;
  resolver 1.1.1.1 1.0.0.1 [2606:4700:4700::1111] [2606:4700:4700::1001]; # Cloudflare

  # Set HSTS to 365 days
  add_header Strict-Transport-Security 'max-age=31536000; includeSubDomains; preload' always;
}
```
