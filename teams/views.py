from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import PlayersForm
from .models import Players


def teams_list(request):
    cursor = connection.cursor()
    cursor.execute('''select * from teams_team''')
    teams = cursor.fetchall()
    return render(request, 'teams/teamslist.html/', {'teams': teams})


def add_player(request):
    cursor = connection.cursor()
    cursor.execute('''select * from teams_team''')
    team = cursor.fetchall()
    form = PlayersForm()
    return render(request, 'teams/addplayer.html', {'form': form, 'team': team})


def save_player(request):
    if request.method == 'POST':
        form_obj = PlayersForm(request.POST, request.FILES)
        if form_obj.is_valid():
            form_obj.save()

            return render(request, 'teams/addplayer.html', {'form': PlayersForm(), 'error': form_obj.errors})

    return HttpResponseRedirect('/teams/')


def team_players(request,id):
    import pdb
    # pdb.set_trace()
    list=Players.objects.filter(team__id=id)
    # cursor=connection.cursor()
    # cursor.execute('''select * from teams_players where team_name =(select team_name from team_team where id={})'''.format(id))
    # list=cursor.fetchall()
    return render(request,'teams/playerlist.html',{'list':list})
