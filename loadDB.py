#!/usr/bin/python

import os
import sys
import requests
import json
#os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
#from django.conf import settings
#from steamapp.models import Player

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

    def getPlayer(self):
        resp_format = "json"
        url = self.url_steamuser + self.player + self.api_key + self.player2 + \
              self.steamid

        r = requests.get(url)
        jsondata = json.loads(r.text)

        print jsondata


if __name__ == "__main__":
    steamClient = SteamClient()
    steamClient.getPlayer()
