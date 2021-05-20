"""cricket app project used in ipl """
import random
from django.db import connection
from django.shortcuts import render
from django.http import HttpResponseRedirect
from teams.forms import PlayersForm
from teams.models import Players, Team, Match, Points


def teams_list(request):
    """ showing all teams and logos """
    cursor = connection.cursor()
    cursor.execute('''select * from teams_team''')
    teams = cursor.fetchall()
    return render(request, 'teams/teamslist.html/', {'teams': teams})


def add_player(request):
    """ adding players to respective teams"""
    import pdb
    # pdb.set_trace()
    cursor = connection.cursor()
    cursor.execute('''select * from teams_team''')
    team = cursor.fetchall()
    print(team)
    form = PlayersForm()
    return render(request, 'teams/addplayer.html', {'form': form, 'team': team})


def save_player(request):
    """ saving player details of adding player"""
    import pdb
    # pdb.set_trace()
    if request.method == 'POST':
        form_obj = PlayersForm(request.POST, request.FILES)
        if form_obj.is_valid():
            form_obj.save()

            return HttpResponseRedirect('/teams/')

    return HttpResponseRedirect('/teams/')


def team_players(request, team_id):
    """ getting all team players individually"""
    # list1 = Players.objects.filter(team__id=id)
    cursor = connection.cursor()
    cursor.execute(f''' select *
from teams_team
join teams_players
on teams_team.id = teams_players.team_id
where teams_team.id = {team_id}''')
    list1 = cursor.fetchall()
    return render(request, 'teams/playerlist.html', {'list': list1})


def player_info(reequest, players_id):
    """ each player information """
    # cursor = connection.cursor()
    # cursor.execute('''select * from teams_players where id={}'''.format(id))
    # player = cursor.fetchone()
    player = Players.objects.get(id=players_id)
    return render(reequest, 'teams/playerinfo.html', {'player': player})


def matches(request):
    """ creating matches"""
    teams = Team.objects.all()
    team1 = random.choice(teams)
    ex = teams.exclude(team_name=team1.team_name)
    team2 = random.choice(ex)
    winner = random.choice((team1, team2))
    win_tm, flag = Points.objects.get_or_create(team=winner)
    Match.objects.create(team1=team1, team2=team2, result=winner)
    win_tm.played += 1
    win_tm.won += 1
    win_tm.points += 2
    win_tm.save()
    if team1.team_name == win_tm.team.team_name:
        l_team = team2
    else:
        l_team = team1
    loss_tm, flag = Points.objects.get_or_create(team=l_team)
    loss_tm.played += 1
    loss_tm.lost += 1
    loss_tm.points += 0
    loss_tm.save()
    flag = False
    if flag:
        return flag
    # cursor=connection.cursor()
    # cursor.execute('''insert into teams_match values("team1","team2","winner")''')
    return render(request, "teams/points_table.html",
                  {"win": win_tm, "loss": loss_tm, "teams": teams})


def points(request):
    """ showing points table"""
    point = Points.objects.all
    return render(request, 'teams/points.html', {'point': point})


def match_hstory(request):
    """ shoeing all matches """
    match = Match.objects.all
    return render(request, 'teams/history.html', {"match": match})
