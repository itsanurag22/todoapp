from django.urls import path
from django.conf.urls import url
from .views import delete_item, index, details, create, delete_list, update_list, delete_item, add_item, mark_item, update_item
app_name='todo'
urlpatterns = [
    path('', index, name='index'),

    path('<int:list_id>/', details, name='list_details'),
    path('create/', create, name='list_create'),
    path('deleteL/<int:list_id>/', delete_list, name='list_delete'),
    path('updateL/<int:list_id2>/', update_list, name='list_update'),
    path('deleteI/<int:item_id>/', delete_item, name='item_delete'),
    path('addI/<int:list_id>/', add_item, name='item_add'),
    path('markI/<int:item_id>/', mark_item, name='item_mark'),
    path('updateI/<int:item_id>/', update_item, name='item_update')



]
