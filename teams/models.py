from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    team_logo = models.ImageField(upload_to='media/')
    club_state = models.CharField(max_length=100)


class Players(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE())
    player_fname = models.CharField(max_length=100)
    player_lname = models.CharField(max_length=100)
    player_image = models.ImageField(upload_to='media1/')
    jersey_number = models.IntegerField(null=False,blank=False)
    player_country = models.CharField(max_length=100)

