from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import PlayersForm
from .models import Players


def teams_list(request):
    """ showing all teams and logos """
    cursor = connection.cursor()
    cursor.execute('''select * from teams_team''')
    teams = cursor.fetchall()
    return render(request, 'teams/teamslist.html/', {'teams': teams})


def add_player(request):
    """ adding players to respective teams"""
    cursor = connection.cursor()
    cursor.execute('''select * from teams_team''')
    team = cursor.fetchall()
    form = PlayersForm()
    return render(request, 'teams/addplayer.html', {'form': form, 'team': team})


def save_player(request):
    """ saving player details of adding player"""
    if request.method == 'POST':
        form_obj = PlayersForm(request.POST, request.FILES)
        if form_obj.is_valid():
            form_obj.save()

            return HttpResponseRedirect('/teams/')

    return HttpResponseRedirect('/teams/')


def team_players(request, id):

    """ getting all team players individually"""
    import pdb
    # pdb.set_trace()
    # list1 = Players.objects.filter(team__id=id)
    cursor=connection.cursor()
    cursor.execute(f''' select *
from teams_team
join teams_players
on teams_team.id = teams_players.team_id
where teams_team.id = {id}''')
    list1=cursor.fetchall()
    return render(request, 'teams/playerlist.html', {'list': list1})


def player_info(reequest,id):
    """ each player information """
    import pdb
    # pdb.set_trace()
    # cursor = connection.cursor()
    # cursor.execute('''select * from teams_players where id={}'''.format(id))
    # player = cursor.fetchone()
    player=Players.objects.get(id=id)
    return render(reequest,'teams/playerinfo.html',{'player':player})