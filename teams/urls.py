from django.urls import path
from . import views
"""creating urls."""

urlpatterns = [
    path('',views.teams_list,name='team_list'),
    path('add_player/',views.add_player,name='add_player'),
    path('save_player/',views.save_player,name='save_player'),
    path('<int:team_id>/team_players/',views.team_players,name='team_players'),
    path('<int:players_id>/player_info/',views.player_info,name='player_info'),
    path('matches/', views.matches, name='matches'),
    path('points/', views.points, name='points'),
    path('history/', views.match_hstory, name='history'),
]