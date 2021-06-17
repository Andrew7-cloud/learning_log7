from django.contrib import admin
from .models import Topic, Entry


# the . before models tells django to search for models.py in same directory as admin.py (this file)

# Register your models (tables) here.
# tells django to manage our model through the admin site
admin.site.register(Topic)
admin.site.register(Entry)
