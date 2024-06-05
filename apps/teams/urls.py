from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.view_teams, name='teams'),
    path('teams/create', views.create_team, name='create_team'),
    path('teams/manage/<int:team_id>', views.manage_team, name='manage_team'),
    path('teams/update/<int:team_id>', views.update_team, name='update_team'),
    path('teams/delete/<int:team_id>', views.delete_team, name='delete_team'),
    path('teams/members/<int:team_id>', views.view_menbers_team, name='view_menbers_team'),
    path('teams/members/create/<int:team_id>', views.create_members_team, name='create_members_team'),
    path('teams/members/manage/<int:team_id>/<int:member_id>', views.manage_members_team, name='manage_members_team'),
    path('teams/members/update/<int:team_id>/<int:member_id>', views.update_members_team, name='update_members_team'),
    path('teams/members/delete/<int:team_id>/<int:member_id>', views.delete_members_team, name='delete_members_team'),
]
