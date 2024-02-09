from django.urls import path 
from .views import (
    home_view,
    task_list,
    create_task,
    delete_task,
    edit_task,
    config,
    del_project,
    report,
) 

app_name = 'task'

urlpatterns = [
    path('', home_view, name='home'),
    path('list/', task_list, name='task_list'),
    path('new/', create_task, name='create_task'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('config/', config, name='config'),
    path('del_project/<int:id>', del_project, name='del_project'),
    path('report/', report, name='report'),
]