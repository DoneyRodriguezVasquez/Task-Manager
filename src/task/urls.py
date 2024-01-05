from django.urls import path 
from .views import (
    home_view,
    create_task,
    task_detail,
    delete_task,
    edit_task,
    config,
    report,
) 

app_name = 'task'

urlpatterns = [
    path('', home_view, name='home'),
    path('config/', config, name='config'),
    path('new/', create_task, name='create_task'),
    path('details/<int:task_id>/', task_detail, name='task_detail'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('report/', report, name='report'),
]