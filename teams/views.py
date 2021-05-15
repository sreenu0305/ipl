from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect


def teams_list(request):
    cursor = connection.cursor()
    cursor.execute('''select * from teams_team''')
    teams=cursor.fetchall()
    return render(request,'teams/teamslist.html/',{'teams':teams})







