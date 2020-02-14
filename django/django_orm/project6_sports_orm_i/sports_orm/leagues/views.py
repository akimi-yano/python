from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		#1 "leagues": League.objects.filter(sport__exact='Baseball'),
		#2 "leagues": League.objects.filter(name__contains='Women'),
		#3 "leagues": League.objects.filter(name__contains='Hockey'),
		#4 "leagues": League.objects.exclude(name__contains='Football'),
		#5 "leagues": League.objects.filter(name__contains='Conference'),
		#6 "leagues": League.objects.filter(name__contains='Atlantic'),
		"teams": Team.objects.all(),
		
		#7 "teams": Team.objects.filter(location__exact="Dallas"),
		#8 "teams": Team.objects.filter(team_name__contains='Raptors'),
		#9 "teams": Team.objects.filter(location__contains='City'),
		#10 "teams": Team.objects.filter(team_name__startswith='T'),
		#11 "teams": Team.objects.all().order_by("location"),
	 	#12 "teams": Team.objects.all().order_by("-team_name"),

		"players": Player.objects.all(),
		#13 "players": Player.objects.filter(last_name ="Cooper")
		#14 "players": Player.objects.filter(first_name = "Joshua"),
		#15 "players": Player.objects.filter(last_name ="Cooper").exclude(first_name = "Joshua")
		#16 "players": Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt"))
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
