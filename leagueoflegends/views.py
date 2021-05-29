from django.shortcuts import render
from .riot import Player

# Create your views here.

def leagueoflegends(request):
    summoner_name_list = ['Xersun', 'Jestem Dawid',
                          'Mateusz0507pl', 'gurnik torfowy', 'Tupolew i brzoza']

    player_list = []

    for summoner_name in summoner_name_list:
        player_list.append(Player(summoner_name))

    swap = True
    while swap:
        swap = False
        for i in range(len(player_list)-1):
            if player_list[i].get_value() < player_list[i+1].get_value():
                player_list[i], player_list[i+1] = player_list[i+1], player_list[i]
                swap = True
    
    context_player_list = []

    for player in player_list:
        context_player_list.append([player.get_summoner_name(
        ), player.get_tier(), player.get_rank(), player.get_league_points()])

    context = {'pl': context_player_list}

    return render(request, 'leagueoflegends/leagueoflegends.html', context=context)
