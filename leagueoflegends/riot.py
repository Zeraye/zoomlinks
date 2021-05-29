from riotwatcher import LolWatcher
import os

LOL_KEY = os.environ.get('LOL_KEY')
lol_watcher = LolWatcher(LOL_KEY)


class Player:
    def __init__(self, summoner_name):
        self.me = lol_watcher.summoner.by_name('eun1', summoner_name)

        if lol_watcher.league.by_summoner('eun1', self.me['id'])[0]['queueType'] == 'RANKED_SOLO_5x5':
            self.number = 0
        else:
            self.number = 1

        self.data = lol_watcher.league.by_summoner(
            'eun1', self.me['id'])[self.number]

    def get_summoner_name(self):
        return self.data['summonerName']

    def get_tier(self):
        return self.data['tier']

    def get_rank(self):
        return self.data['rank']

    def get_league_points(self):
        return self.data['leaguePoints']

    def get_value(self):
        rank_list = {'IRON': 0, 'BRONZE': 1, 'SILVER': 2, 'GOLD': 3, 'PLATINUM': 4,
                     'DIAMOND': 5, 'MASTER': 6, 'GRANDMASTER': 7, 'CHALLENGER': 8}
        tier_list = {'I': 4, 'II': 3, 'III': 2, 'IV': 1}
        value = rank_list[self.get_tier()]*1000 + tier_list[self.get_rank()] * \
            100 + int(self.get_league_points())
        return value
