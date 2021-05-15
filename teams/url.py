from django.urls import path
from . import views


urlpatterns=[
    path('',views.teams_list,name='team_list'),
]