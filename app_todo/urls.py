from django.urls import path 
from .views import task_list, task_detail , task_create , task_delate, task_update



urlpatterns = [
    path('tasks/', task_list),
    path('task/<int:pk>/', task_detail),
    path('task_create/', task_create),
    path('task_delete/<int:pk>/', task_delate),
    path('task_update/<int:pk>/', task_update)
]