from django import forms

from .models import Topic, Entry

# class inherets from forms (django class)
# models.py function named Topic represents a db table
# table passed model and fields selected is only the text field
# labels = {'text': ''} tells django not to generate a label for the text field
# simplest version of ModelForm is a nested meta class telling django which model (db) to base the form on and which fields to include.


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
