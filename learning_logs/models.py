from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# a model tells django how to work with data stroed in app

# table name is Topic, text and date_added are the two fields.

# the below adds a field to the Topic table (class) & Associates the login uder id with each topic
# owner = models.ForeignKey(User, on_delete=models.CACSCADE)


class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # Return a string representation of the model
        return self.text

# self.text is an instance of text


class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

        def __str__(self):
            """Return a string representation of the model"""
            return f"{self.text[:50]}..."
