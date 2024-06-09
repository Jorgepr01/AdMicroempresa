from django.urls import path
from . import views

urlpatterns = [
    path('project/version/<int:project_version_id>/tasks/', views.view_tasks, name='view_tasks'),
    path('project/version/<int:project_version_id>/tasks/completed/', views.view_completed_tasks, name='view_completed_tasks'),
    path('project/version/tasks/create/', views.create_task, name='create_task'),
    path('project/version/tasks/manage/<int:taks_id>/', views.manage_task, name='manage_task'),
    path('project/version/tasks/update/<int:taks_id>/', views.update_task, name='update_task'),
    path('project/version/tasks/complete/<int:taks_id>/', views.complete_task, name='complete_task'),
    path('project/version/tasks/delete/<int:taks_id>/', views.delete_task, name='delete_task'),
    path('project/version/<int:project_version_id>/tasks/all/', views.view_all_tasks, name='view_all_tasks'),
]