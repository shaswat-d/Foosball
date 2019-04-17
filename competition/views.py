from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.views.generic import CreateView
from django.db.models import Q
from django.urls import reverse_lazy, reverse

from .models import Team, Competition, Match
from .forms import CreateTeamForm, CreateCompForm, CreateMatchForm


class createTeamView(CreateView):
    template_name = "team/form.html"
    form_class = CreateTeamForm

    def get_success_url(self):
        return reverse('team-detail', kwargs={'pk': self.object.id})


class createCompView(CreateView):
    template_name = "competition/form.html"
    form_class = CreateCompForm
    success_url = reverse_lazy("home")


class createMatchView(CreateView):
    template_name = "match/form.html"
    form_class = CreateMatchForm
    success_url = reverse_lazy("home")


def getTeam(team):
    p1 = team.player1
    p2 = team.player2
    tm = Team.objects.filter(Q(player1=p1) & Q(player2=p2))
    return tm


def createMatch(request):
    if request.method == 'POST':
        form = CreateMatchForm(request.POST)
        if form.is_valid():
            match = Match()
            match.game = form.cleaned_data.get('game')
            match.team1 = form.cleaned_data.get('team1')
            match.team2 = form.cleaned_data.get('team2')
            match.team1_score = form.cleaned_data.get('team1_score')
            match.team2_score = form.cleaned_data.get('team2_score')
            match.comptn = form.cleaned_data.get('comptn')
            match.save()
            print(match.game)
            if match.team1_score > match.team2_score:
                if match.game == 'TT':
                    match.team1.tt_points += 3
                    match.team2.tt_points -= 1
                else:
                    match.team1.foosball_points += 3
                    match.team2.foosball_points -= 1
            elif match.team1_score < match.team2_score:
                if match.game == 'TT':
                    match.team2.tt_points += 3
                    match.team1.tt_points -= 1
                else:
                    match.team2.foosball_points += 3
                    match.team1.foosball_points -= 1
            match.team1.save()
            match.team2.save()
            return redirect("leaderboard", type=match.game)
    else:
        form = CreateMatchForm()
    return render(request, 'match/form.html', {'form': form})


def teamDetail(request, pk):
    team = Team.objects.get(pk=pk)
    matches = Match.objects.filter(Q(team1=team) | Q(team2=team))
    content = {
        'team': team,
        'matches': matches
    }
    return render(request, 'team/detail.html', {'content': content})


def showLeaderboard(request, type):
    if type == 'FS' or type == 'foosball':
        teams = Team.objects.all().order_by('-foosball_points')[:100]
    else:
        teams = Team.objects.all().order_by('-tt_points')[:10]
    return render(request, 'leaderboard.html', {'teams': teams})


def home(request):
    return HttpResponse("Welcome to the Foosball Tournament!")
