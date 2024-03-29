from django import forms

from .models import Player, Team, Match, Competition


class CreatePlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name']


class CreateTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['player1', 'player2']


class CreateCompForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['title', 'type', 'place']


class CreateMatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['team1', 'team2', 'team1_score', 'team2_score', 'game']
