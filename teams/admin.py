from django.contrib import admin
# Register your models here.
from teams.models import Team,Players

admin.site.register(Team)
admin.site.register(Players)
