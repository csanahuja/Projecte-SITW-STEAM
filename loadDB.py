import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "steam.settings")
django.setup()

from steamapp.models import Player
import sys
import requests
import json
import pycountry

"""
Program that loads the data obtained from STEAM-API to the database
API STEAM Key = 070D3A2B5CFB0B9BD4C162C0BC82E25E
STEAM-ID (64-bit) of Palm Desert (Random Subject) = 76561197982003783
"""

#p1 = Player("2342","Gaben","nothere","private","offline")
#p1.save()


class SteamClient():

    def __init__(self):
        self.api_key = "070D3A2B5CFB0B9BD4C162C0BC82E25E"
        self.steamid = "76561197982003783"
        self.url_steamuser = "http://api.steampowered.com/ISteamUser/"
        self.player = "GetPlayerSummaries/v0002/?key="
        self.player2 = "&steamids="
        self.friend = "GetFriendList/v0001/?key="
        self.friend2 = "&steamid="
        self.friend3 = "&relationship=friend"

    def getFriends(self):
        url = self.url_steamuser + self.friend + self.api_key + self.friend2 + \
              self.steamid + self.friend3
        r = requests.get(url)
        jsondata = json.loads(r.text)

        friends = jsondata.get("friendslist").get("friends")

        i = 0
        for friend in friends:
            if i == 100:
                break
            steamClient.getPlayer(friend.get("steamid"))
            print "Saved friend num: " + str(i+1) + " out of 100"
            i += 1

    def getPlayer(self, steamid):
        url = self.url_steamuser + self.player + self.api_key + self.player2 + steamid
        r = requests.get(url)
        jsondata = json.loads(r.text)

        player = jsondata.get("response").get("players")[0]

        privacy = "private"
        if player.get("communityvisibilitystate") == 3:
            privacy = "public"

        country_code = player.get("loccountrycode")
        country_name = ""
        if country_code != None:
            country = pycountry.countries.get(alpha2=country_code)
            country_name = country.name

        p = Player(steamid, player.get("personaname"), player.get("profileurl"), \
            privacy, country_name, player.get("lastlogoff"))
        p.save()


if __name__ == "__main__":
    steamClient = SteamClient()
    steamClient.getPlayer('76561197982003783')
    steamClient.getFriends()
