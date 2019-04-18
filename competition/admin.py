from django.contrib import admin

# Register your models here.
from .models import Player, Team, Match, Competition


admin.site.register(Match)
admin.site.register(Team)
admin.site.register(Competition)
admin.site.register(Player)
