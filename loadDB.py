import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "steam.settings")
django.setup()

from steamapp.models import Player, Game
import sys
import requests
import json
import pycountry

"""
Program that loads the data obtained from STEAM-API to the database
API STEAM Key = 070D3A2B5CFB0B9BD4C162C0BC82E25E
STEAM-ID (64-bit) of Palm Desert (Random Subject) = 76561197982003783
"""


class SteamClient():

    def __init__(self):
        self.api_key = "070D3A2B5CFB0B9BD4C162C0BC82E25E"
        self.steamid = "76561197982003783"
        self.url_base = "http://api.steampowered.com/"
        self.service_user = "ISteamUser/"
        self.service_player = "IPlayerService/"
        self.player = "GetPlayerSummaries/v0002/?key="
        self.player2 = "&steamids="
        self.friend = "GetFriendList/v0001/?key="
        self.friend2 = "&steamid="
        self.friend3 = "&relationship=friend"
        self.owngames = "GetOwnedGames/v0001/?key="
        self.owngames2 = "&steamid="
        self.owngames3 = "&include_appinfo=1"
        self.steamids = []
        self.games = []


    def getFriends(self):
        url = self.url_base + self.service_user + self.friend + self.api_key + \
              self.friend2 + self.steamid + self.friend3
        r = requests.get(url)
        jsondata = json.loads(r.text)

        friends = jsondata["friendslist"]["friends"]

        steamClient.getAndSavePlayer(self.steamid)

        i = 0
        for friend in friends:
            if i == 99:
                break
            steamClient.getAndSavePlayer(friend["steamid"])
            print "Saved friend num: " + str(i+1) + " out of 99"
            i += 1


    def getAndSavePlayer(self, steamid):
        self.steamids.append(steamid)

        url = self.url_base + self.service_user + self.player + self.api_key + \
              self.player2 + steamid
        r = requests.get(url)
        jsondata = json.loads(r.text)

        player = jsondata["response"]["players"][0]

        privacy = "private"
        if player["communityvisibilitystate"] == 3:
            privacy = "public"

        country_code = player["loccountrycode"]
        country_name = ""
        if country_code != None:
            country = pycountry.countries.get(alpha2=country_code)
            country_name = country.name

        p = Player(steamid, player["personaname"], player["profileurl"], \
            privacy, country_name, player.get["lastlogoff"])
        p.save()


    def getOwnedGames(self, steamid):
        url = self.url_base + self.service_player + self.owngames + self.api_key + \
              self.owngames2 + steamid + self.owngames3
        r = requests.get(url)
        jsondata = json.loads(r.text)

        games = jsondata["response"]["games"]
        i = 0
        for game in games:
            if i == 1000:
                break
            self.saveGame(game["appid"],game["name"])
            print "Saved game num: " + str(i+1) + " out of 1000"
            i += 1


    def saveGame(self, appid, name):
        g = Game(appid, name)
        g.save()


if __name__ == "__main__":
    steamClient = SteamClient()

    #steamClient.getFriends()
    steamClient.getOwnedGames('76561197982003783')
