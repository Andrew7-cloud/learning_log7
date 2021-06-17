"""Defines URL patterns for learning_logs"""
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


from django.urls import path

from . import views
# name of URL is index, we will reference in views.py

app_name = 'learning_logs'


urlpatterns = [
    # home page: path, function to call, path name
    path('', views.index, name='index'),

    # page that shows all of the Topics
    path('topics/', views.topics, name='topics'),

    # page that shows all entries for a single topic. <int:topic_id> captures the integer value between /integer/
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # add a page to allow users to add a topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # page that shows all entries for a single topic. <int:topic_id> captures the integer value between /integer/
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # page that shows all entries for a single topic. <int:topic_id> captures the integer value between /integer/
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
