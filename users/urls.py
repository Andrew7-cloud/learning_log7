"""Defines URL patterns for users"""
# docstring to define which url.py we are working with
# path function is needed when mapping URL's to the Views module (dot tells python to import the views.py in the same directory as urls.py)
# the variable app_name helps django determine this urls.py file from files of the same name - in other apps
# urlpatterns variable is a list of individual pages that can be requested from the learning_logs app
# the actual URL pattern is a call to the path() functions, which takes 3 arguments

# 1 a string that helps django route the request properly (receives requested URL ans tries to route request to a view)
# (searches all URLpatterns we've defined to find one that matches the current request
# django ignores the the base url so the empty string matches the base URL
# any other URL will not match this pattern and will produce error)

# second argmument in path() specifies which function to call in views.py
# when a requested URL matches the pattern we are defining, django calls the index() function from the views.py (we will write this function next)

# third argument provides the name index for this URL pattern so we can refer to it in other code sections
# when we want to provide a link to the home page, we will use this name instead of writing out a URL

from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    # home page: path, function to call, path name
    # include defaullt auth urls
    path('', include('django.contrib.auth.urls')),

    # Registration Page
    path('register/', views.register, name='register'),

]
