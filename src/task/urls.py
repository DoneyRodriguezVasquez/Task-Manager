from django.urls import path 
from .views import (
    home_view,
    task_detail,
    edit_task,
    ListTasksView,
) 

app_name = 'task'

urlpatterns = [
    path('', home_view, name='home'),
    path('list/', ListTasksView.as_view(), name='tasks'),
    path('details/<int:task_id>/', task_detail, name='task_detail'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
]