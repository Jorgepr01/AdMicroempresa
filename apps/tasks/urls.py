from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.view_tasks, name='view_tasks'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/manage/<int:taks_id>/', views.manage_task, name='manage_task'),
    path('tasks/update/<int:taks_id>/', views.update_task, name='update_task'),
    path('tasks/complete/<int:taks_id>/', views.complete_task, name='complete_task'),
    path('tasks/delete/<int:taks_id>/', views.delete_task, name='delete_task'),
]