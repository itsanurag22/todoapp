from django.urls import path
from django.conf.urls import url
from .views import deleteItem, index, details, create, deleteList, updateList, deleteItem, addItem, markItem, updateItem
app_name='todo'
urlpatterns = [
    path('', index, name='index'),

    path('<int:list_id>/', details, name='list_details'),
    path('create/', create, name='list_create'),
    path('deleteL/<int:list_id>/', deleteList, name='list_delete'),
    path('updateL/<int:list_id2>/', updateList, name='list_update'),
    path('deleteI/<int:item_id>/', deleteItem, name='item_delete'),
    path('addI/<int:list_id>/', addItem, name='item_add'),
    path('markI/<int:item_id>/', markItem, name='item_mark'),
    path('updateI/<int:item_id>/', updateItem, name='item_update')



]
