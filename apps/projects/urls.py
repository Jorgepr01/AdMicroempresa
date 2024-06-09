from django.urls import path
from . import views

urlpatterns = [
    # path('manage_project/', views.manage_project, name='manage_project'),
    path('', views.index, name='home'),
    path('project/', views.view_project, name='view_project'),
    path('project/create/', views.create_projects, name='create_project'),
    path("project/manage/<int:project_id>", views.manage_project, name="manage_project"),
    path("project/update/<int:project_id>", views.update_project, name="update_project"),
    path("project/complete/<int:project_id>", views.complete_project, name="complete_project"),
    path("project/delete/<int:project_id>", views.delete_project, name="delete_project"),
    path("project/version/<int:project_id>", views.view_project_versions, name="view_project_versions"),
    path("project/version/create/<int:project_id>", views.create_project_version, name="create_project_version"),
    path("project/version/manage/<int:project_id>/<int:project_version_id>", views.manage_project_version, name="manage_project_version"),
    path("project/version/update/<int:project_id>/<int:project_version_id>", views.update_project_version, name="update_project_version"),
    path("project/version/delete/<int:project_id>/<int:project_version_id>", views.delete_project_version, name="delete_project_version"),
    path("project/member/<int:project_id>", views.view_menbers_project, name="view_menbers_project"),
    path("project/member/create/<int:project_id>", views.create_members_project, name="create_members_project"),
    path("project/member/manage/<int:project_id>/<int:member_id>", views.manage_members_project, name="manage_members_project"),
    path("project/member/update/<int:project_id>/<int:member_id>", views.update_members_project, name="update_members_project"),
    path("project/member/delete/<int:project_id>/<int:member_id>", views.delete_members_project, name="delete_members_project"),
]
