from django.contrib import admin
# Register your models here.
from teams.models import Team, Players, Match, Points

admin.site.register(Team)
admin.site.register(Players)
admin.site.register(Match)
admin.site.register(Points)
