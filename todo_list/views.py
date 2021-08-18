from django.shortcuts import redirect, render
import datetime
from django.http import HttpResponse, Http404
from .models import TodoList, TodoItem
from django.template import loader
from django.urls import path
from .forms import Itemform


def index(request):
    """For showing the index(main) page consisting of all the lists."""
    todolists = TodoList.objects.all()
    template = loader.get_template('todo_list/index.html')
    context = {
        'todolists': todolists,
    }
    return render(request, 'todo_list/index.html', context)


def details(request, list_id):
    """For showing the details page consisting of all the items of a list."""
    try:
        todolist = TodoList.objects.get(id=list_id)
    except TodoList.DoesNotExist:
        raise Http404("This List Does not Exists")
    items_list = TodoItem.objects.filter(todo_list=todolist)
    template = loader.get_template('todo_list/details.html')
    context = {
        'todolist': todolist,
        'items_list': items_list
    }
    return render(request, 'todo_list/details.html', context)


def create(request):
    """Create a list."""
    template = loader.get_template('todo_list/createlist.html')
    if request.method == "GET":
        return render(request, 'todo_list/createlist.html')
    elif request.method == "POST":
        name = request.POST["name"]
        try:
            test=TodoList.objects.get(list_name=name)
        except TodoList.DoesNotExist:
            test = None
        except TodoList.MultipleObjectsReturned:
            raise Http404("This List name already exists")
        if test is None: 
            TodoList.objects.create(list_name=name)
            lists = TodoList.objects.all()
            context = {
                'todolists': lists,
            }
            return render(request, 'todo_list/index.html', context)
        else:
            raise Http404("This List name already exists")


def delete_list(request, list_id):
    """Deletes a list."""
    try:
        todolist = TodoList.objects.get(id=list_id)
    except TodoList.DoesNotExist:
        raise Http404("This List Does not Exists")
    if todolist:
        todolist.delete()
        return redirect(f'/todo_list')


def update_list(request, list_id):
    """Updates an existing list."""
    template = loader.get_template('todo_list/updatelist.html')
    try:
        todolist = TodoList.objects.get(id=list_id)
    except TodoList.DoesNotExist:
        raise Http404("This List Does not Exists")
    if request.method == "GET":
        return render(request, 'todo_list/updatelist.html')
    elif request.method == "POST":
        name = request.POST["name"]
        check = TodoList.objects.get(list_name= name)
        if not check:
            todolist.list_name = name
            todolist.save()
            lists = TodoList.objects.all()
            context = {
                'todolists': lists,
            }
            return render(request, 'todo_list/index.html', context)
        else:
            raise Http404("This List name already exists. Try another name")


def delete_item(request, item_id):
    """Deletes an item from a list."""
    try:
        todoitem = TodoItem.objects.get(id=item_id)    
    except TodoItem.DoesNotExist:
        raise Http404("This Item Does not Exists")
    if todoitem:
        listID = todoitem.todo_list.id
        todoitem.delete()
        return redirect(f'/todo_list/{listID}')
    else:
        raise Http404("This Item Does not Exists")


def add_item(request, list_id):
    """Adds an item to an existing list."""
    todolist = TodoList.objects.get(id=list_id)
    if request.method == "POST":
        form = Itemform(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            object.todo_list = todolist
            object.save()
            return redirect(f'/todo_list/{list_id}')
    form = Itemform()
    context = {
        "item_info" : form
    }
    return render(request, 'todo_list/additem.html', context)


def mark_item(request, item_id):
    """To mark an item(task) as done."""
    try:
        todoitem = TodoItem.objects.get(id=item_id)
    except TodoList.DoesNotExist:
        raise Http404("This Item Does not Exists")
    listID = todoitem.todo_list.id
    todoitem.checked = True
    todoitem.save()
    return redirect(f'/todo_list/{listID}')


def update_item(request, item_id):
    """Updates an already existing item(task)."""
    form = Itemform()
    try:
        todoitem = TodoItem.objects.get(id=item_id)
        
    except TodoItem.DoesNotExist:
        raise Http404("This Item Does not Exists")
    list_id = todoitem.todo_list.id
    form = Itemform(request.POST or None, instance=todoitem)
    if form.is_valid():
        form.save()
        return redirect(f'/todo_list/{list_id}')
    
    context = {
        "update_info" : form
    }
    return render(request, 'todo_list/updateitem.html', context)


    
    
    
    
    


 


    

    

