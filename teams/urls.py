from django.urls import path
from . import views


urlpatterns=[
    path('',views.teams_list,name='team_list'),
    path('add_player/',views.add_player,name='add_player'),
    path('save_player/',views.save_player,name='save_player'),
    path('<int:id>/team_players/',views.team_players,name='team_players'),

]