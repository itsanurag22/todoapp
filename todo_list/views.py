from django.shortcuts import redirect, render
import datetime
from django.http import HttpResponse, Http404
from .models import TodoList, TodoItem
from django.template import loader
from django.urls import path
from .forms import Itemform

def index(request):
    todolists = TodoList.objects.all()
    # items = TodoItem.objects.all()
    template = loader.get_template('todo_list/index.html')
    context = {
        'todolists': todolists,
    }
    return render(request, 'todo_list/index.html', context)

def details(request, list_id):
    try:
        todolist = TodoList.objects.get(id=list_id)
    except TodoList.DoesNotExist:
        raise Http404("This List Does not Exists")
    items_list = TodoItem.objects.filter(todo_list=todolist)
    context = {
        'todolist': todolist,
        'items_list': items_list
    }
    return render(request, 'todo_list/details.html', context)

def create(request):
    if request.method == "GET":
        return render(request, 'todo_list/createlist.html')
    
    name = request.POST["name"]
    # task = request.POST["task"]
    # due = str(request.POST["due"])
    try:
        test=TodoList.objects.get(list_name=name)
    except TodoList.DoesNotExist:
        test = None
    except TodoList.MultipleObjectsReturned:
        raise Http404("This List name already exists")
    if test is None: 
        TodoList.objects.create(list_name=name)
        # t = TodoList.objects.get(list_name=name)

        
        lists = TodoList.objects.all()
        # TodoItem.objects.create(title=task, checked=False, due_date=due, todo_list=t)

        context = {
            'todolists': lists,
        }
        return render(request, 'todo_list/index.html', context)

def deleteList(request, list_id):
    try:
        todolist = TodoList.objects.get(id=list_id)
    except TodoList.DoesNotExist:
        raise Http404("This List Does not Exists")
    if todolist:
        todolist.delete()
    # lists = TodoList.objects.all()
    #     # TodoItem.objects.create(title=task, checked=False, due_date=due, todo_list=t)

    # context = {
    #     'todolists': lists,
    # }
    # return render(request, 'todo_list/index.html', context)
        return redirect(f'/todo_list')

def updateList(request, list_id2):
    try:
        todolist = TodoList.objects.get(id=list_id2)
    except TodoList.DoesNotExist:
        raise Http404("This List Does not Exists")
    if request.method == "GET":
        return render(request, 'todo_list/updatelist.html')
    name2 = request.POST["name2"]
    # todolist.update(list_name = "name2")
    todolist.list_name = name2
    todolist.save()

    lists = TodoList.objects.all()
        # TodoItem.objects.create(title=task, checked=False, due_date=due, todo_list=t)

    context = {
        'todolists': lists,
    }
    return render(request, 'todo_list/index.html', context)

def deleteItem(request, item_id):
    try:
        todoitem = TodoItem.objects.get(id=item_id)    
    except TodoItem.DoesNotExist:
        raise Http404("This Item Does not Exists")
    if todoitem:
        listID = todoitem.todo_list.id
        todoitem.delete()
        # return redirect('/lecture/todo_list/templates/todo_list/index.html')
        return redirect(f'/todo_list/{listID}')

def addItem(request, list_id):
#     if request.method == "GET":
#         return render(request, 'todo_list/additem.html')
#     todolist = TodoList.objects.get(id=list_id)
#     task = request.POST["task"]
#     due = request.POST["due"]
#     done=bool(request.POST["check"])
#     find_items = TodoItem.objects.get(title=task, due_date = due)
#     if find_items:
#         raise Http404("This Item already exists")
#     else:
#         TodoItem.objects.create(title=task, due_date = due, checked=done, todo_list=todolist)
#         return redirect(f'/todo_list/{list_id}')
    todolist = TodoList.objects.get(id=list_id)
    if request.method == "POST":
        form = Itemform(request.POST)
        if form.is_valid():
            # form=form.cleaned_data
            # form['todo_list'] = todolist
            object = form.save(commit=False)
            object.todo_list = todolist
            object.save()
            return redirect(f'/todo_list/{list_id}')
    form = Itemform()
    context = {
        "item_info" : form
    }
    return render(request, 'todo_list/additem.html', context)
def markItem(request, item_id):
    try:
        todoitem = TodoItem.objects.get(id=item_id)
    except TodoList.DoesNotExist:
        raise Http404("This Item Does not Exists")
    listID = todoitem.todo_list.id
    todoitem.checked = True
    todoitem.save()
    return redirect(f'/todo_list/{listID}')

def updateItem(request, item_id):
    form = Itemform()
    try:
        todoitem = TodoItem.objects.get(id=item_id)
        
    except TodoList.DoesNotExist:
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

    
    
    
    
    


 


    

    



    







# Create your views here.
