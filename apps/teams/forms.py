from django import forms
from .models import Team, TeamMember

class FormTeam(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Team Name'}),
        }


class FormTeamMember(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['user','team','role']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-select'}),
            'team': forms.Select(attrs={'class': 'form-select'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Role'}),
        }
