from django import forms
from django.forms import DateTimeInput
from .models import TodoItem, TodoList
class datetime(forms.DateTimeInput):
    input_type = 'datetime-local'
class Itemform(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'checked', 'due_date']
        exclude = ('todo_list',) 
        
        widgets = {'due_date': datetime()}

