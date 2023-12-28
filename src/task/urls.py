from django.urls import path 
from .views import (
    home_view,
    ListTasksView,
) 

app_name = 'task'

urlpatterns = [
    path('', home_view, name='home'),
    path('list/', ListTasksView.as_view(), name='tasks'),
]