from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count, Q

from . import team_maker

def index(request):
	# Level II (1)
	# atlanticLeague = League.objects.filter(name__exact="Atlantic Soccer Conference")[0]
	# print(atlanticLeague)

	# LevelII (2)
	# bp = Team.objects.filter(team_name__contains="Penguins").filter(location__contains="Boston")[0]
	# print(bp)

	# LevelII (3)
	# icbc = League.objects.filter(name__exact="International Collegiate Baseball Conference")[0]
	# teams_icbc =icbc.teams.all()
	# print(teams_icbc)

	# LevelII (4)
	# acaf = League.objects.filter(name__exact="American Conference of Amateur Football")[0]
	# teams_acaf =acaf.teams.all()
	# print(teams_acaf)

	# LevelII (5)
	# football_leagues = League.objects.filter(sport__iexact="Football")
	# football_teams = Team.objects.filter(league__in = football_leagues)
	# football_players = Player.objects.filter(curr_team__in = football_teams)
	# print(football_teams)
	# print(football_teams.count())
	# print(football_players)

	# LevelII (5)
	# football_teams = Team.objects.filter(league__sport__iexact="Football")
	# football_players = Player.objects.filter(curr_team__in = football_teams)
	# print(football_teams)
	# print(football_teams.count())


	# LevelII (6)
	# sophias = Player.objects.filter(first_name__exact = "Sophia")
	# team_with_sophia = Team.objects.filter(curr_players__in=sophias)
	# print(team_with_sophia)

	# LevelII (７)
	# sophias = Player.objects.filter(first_name__exact = "Sophia")
	# team_with_sophia = Team.objects.filter(curr_players__in=sophias)
	# leagues_with_sophia = League.objects.filter(teams__in=team_with_sophia)
	# print(leagues_with_sophia)


	# LevelII (8)
	# teams_except_wr = Team.objects.exclude(team_name__iexact="Roughriders")
	# players_who_dont_play_for_wr = Player.objects.filter(curr_team__in=teams_except_wr)
	# print(players_who_dont_play_for_wr)

	# LevelII (9)
	# samuel_evans = Player.objects.filter(first_name="Samuel").filter(last_name="Evans")
	# all_teams_sam_played = Team.objects.filter(curr_players__in=samuel_evans)
	# print(all_teams_sam_played)

	# LevelII (10)
	# tiger_cats = Team.objects.filter(team_name="Tiger-Cats")
	# players_with_tc = Player.objects.filter(all_teams__in=tiger_cats)
	# print(players_with_tc)

	# LevelII (11)
	# vikings = Team.objects.filter(team_name="Vikings")
	# players_with_v_curr = Player.objects.filter(curr_team__in=vikings)
	# print(players_with_v_curr.count())
	# players_with_v_all = Player.objects.filter(all_teams__in=vikings)
	# print(players_with_v_all.count())

	# LevelII (11)
	#Testing with the team whose current is not empty
	# vikings = Team.objects.filter(team_name="Tiger-Cats")
	# players_with_v_curr = Player.objects.filter(curr_team__in=vikings)
	# print(players_with_v_curr.count())
	# players_with_v_all = Player.objects.filter(all_teams__in=vikings)
	# print(players_with_v_all.count())

	# LevelII (12)
	# jg = Player.objects.filter(first_name="Jacob").filter(last_name="Gray")
	# teams_jp_all = Team.objects.filter(all_players__in=jg)
	# print(teams_jp_all)
	# teams_jp_curr = Team.objects.filter(curr_players__in=jg)
	# print(teams_jp_curr)

	# LevelII (13)
	# league_afabp = League.objects.filter(name ="Atlantic Federation of Amateur Baseball Players")
	# teams_played_league = Team.objects.filter(league__in=league_afabp)
	# players_league = Player.objects.filter(all_teams__in=teams_played_league)
	
	#for testing
	# joshua = Player.objects.filter(first_name="Joshua")
	# print(joshua.count())


	# LevelII (14)
	# all the codes are in the context below

	


	context = {
		"leagues": League.objects.all(),
		#1 "leagues": League.objects.filter(sport__exact='Baseball'),
		#2 "leagues": League.objects.filter(name__contains='Women'),
		#3 "leagues": League.objects.filter(name__contains='Hockey'),
		#4 "leagues": League.objects.exclude(name__contains='Football'),
		#5 "leagues": League.objects.filter(name__contains='Conference'),
		#6 "leagues": League.objects.filter(name__contains='Atlantic'),
		# "leagues": League.objects.teams.filter(name__exact="Atlantic Soccer Conference"),

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

		# Level II (1)
		# "league": atlanticLeague,
		# "atlanticTeams": Team.objects.filter(league=atlanticLeague),

		# Level II (2)
		# "bp_curr_players": Player.objects.filter(curr_team=bp)

		# Level II (3)
		# "icbc_teams":teams_icbc

		# Level II (4)
		# "teams_acaf": teams_acaf

		# Level II (5)
		# "football_teams": football_teams,
		# "football_players": football_players

		# LevelII (6)
		# "team_with_sophia": team_with_sophia,

		# LevelII (７)
		# "leagues_with_sophia": leagues_with_sophia

		# LevelII (8)
		# "players_who_dont_play_for_wr": players_who_dont_play_for_wr

		# LevelII (9)
		# "all_teams_sam_played": all_teams_sam_played

		# LevelII (10)
		# "players_with_tc": players_with_tc

		# LevelII (11)
		# "players_with_v_all": players_with_v_all,
		# "players_with_v_curr": players_with_v_curr

		# LevelII (12)
		# "teams_jp_all": teams_jp_all,
		# "teams_jp_curr": teams_jp_curr
		
		# LevelII (13)
		# "players_league": players_league,

		# LevelII (14)
        # None of the teams have more than 8 curr_players
		# "test": Team.objects.annotate(player_count=Count('curr_players')).filter(player_count__gte=12)
		
		#The below is the answer:
		# "test": Team.objects.annotate(player_count=Count('all_players')).filter(player_count__gte=12)
		
		# LevelII (15)
		"test": Player.objects.annotate(team_count=Count('all_teams')).order_by('-team_count')

	}
	# print(Team.objects.annotate(Count('curr_players')).filter(curr_players__count__gt=12))
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
