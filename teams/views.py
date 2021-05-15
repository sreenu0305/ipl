from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .forms import PlayersForm


def teams_list(request):
    cursor = connection.cursor()
    cursor.execute('''select * from teams_team''')
    teams=cursor.fetchall()
    return render(request,'teams/teamslist.html/',{'teams':teams})


def add_player(request):
    cursor = connection.cursor()
    cursor.execute('''select * from teams_team''')
    team=cursor.fetchall()
    form = PlayersForm()
    return render(request,'teams/addplayer.html',{'form':form,'team':team})


def save_player(request):
    if request.method =='POST':
        form_obj = PlayersForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()

            return render(request, 'teams/addplayer.html', {'form': PlayersForm(), 'error': form_obj.errors})

    return HttpResponseRedirect('/teams/')




