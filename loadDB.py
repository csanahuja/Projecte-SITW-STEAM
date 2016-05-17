#!/usr/local/bin/python
# coding: utf-8
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "steam.settings")
django.setup()

from steamapp.models import Player, Game, OwnedGame, Achievement, \
                            OwnedAchievement, Ban
import sys
import requests
import json
import pycountry

"""
Program that loads the data obtained from STEAM-API to the database
API STEAM Key = 070D3A2B5CFB0B9BD4C162C0BC82E25E
STEAM-ID (64-bit) of Palm Desert (Random Subject) = 76561197982003783
APPID Garry's Mod (Game with Achievements) = 4000
"""


class SteamClient():

    def __init__(self):
        self.api_key = "070D3A2B5CFB0B9BD4C162C0BC82E25E"
        self.steamid = "76561197982003783"
        self.appid = "4000"
        self.url_base = "http://api.steampowered.com/"
        self.service_user = "ISteamUser/"
        self.service_user_stats = "ISteamUserStats/"
        self.service_player = "IPlayerService/"
        self.player = "GetPlayerSummaries/v0002/?key="
        self.player2 = "&steamids="
        self.friend = "GetFriendList/v0001/?key="
        self.friend2 = "&steamid="
        self.friend3 = "&relationship=friend"
        self.owngames = "GetOwnedGames/v0001/?key="
        self.owngames2 = "&steamid="
        self.owngames3 = "&include_appinfo=1"
        self.achievements = "GetSchemaForGame/v2/?key="
        self.achievements2 = "&appid="
        self.ownachievements = "GetPlayerAchievements/v0001/?appid="
        self.ownachievements2 = "&key="
        self.ownachievements3 = "&steamid="
        self.ban = "GetPlayerBans/v1/?key="
        self.ban2 = "&steamids="
        self.steamids = {}
        self.games = {}
        self.achievement_ids = {}
        self.id_ownedgames = 0
        self.id_ownedachievements = 0
        self.id_achievements = 0




    def getFriends(self):
        url = self.url_base + self.service_user + self.friend + self.api_key + \
              self.friend2 + self.steamid + self.friend3
        r = requests.get(url)
        jsondata = json.loads(r.text)

        friends = jsondata["friendslist"]["friends"]

        steamClient.getAndSavePlayer(self.steamid)

        i = 0
        for friend in friends:
            if i == 100:
                break
            steamClient.getAndSavePlayer(friend["steamid"])
            i += 1


    def getAndSavePlayer(self, steamid):
        url = self.url_base + self.service_user + self.player + self.api_key + \
              self.player2 + steamid
        r = requests.get(url)
        jsondata = json.loads(r.text)

        player = jsondata["response"]["players"][0]

        self.steamids[steamid] = player["personaname"]

        privacy = "private"
        if player["communityvisibilitystate"] == 3:
            privacy = "public"

        country_code = player.get("loccountrycode")
        country_name = ""
        if country_code != None:
            country = pycountry.countries.get(alpha2=country_code)
            country_name = country.name

        p = Player(steamid, player["personaname"], player["profileurl"], \
            privacy, country_name, player["lastlogoff"])
        p.save()


    def getOwnedGames(self, steamid):
        url = self.url_base + self.service_player + self.owngames + self.api_key + \
              self.owngames2 + steamid + self.owngames3
        r = requests.get(url)
        jsondata = json.loads(r.text)

        games = jsondata["response"].get("games")
        if games != None:
            i = 0
            for game in games:
                if i == 50:
                    break
                if self.games.has_key(game["appid"]) == False:
                    self.games[game["appid"]] = game["name"]
                    self.saveGame(game["appid"],game["name"])
                self.saveOwnedGame(steamid, game["appid"], game["playtime_forever"])
                i += 1


    def saveGame(self, appid, name):
        g = Game(appid, name)
        g.save()

    def saveOwnedGame(self, steamid, appid, playedtime):
        og = OwnedGame(self.id_ownedgames, steamid, appid, \
                        self.steamids[steamid], self.games[appid], playedtime)
        self.id_ownedgames += 1
        og.save()


    def getAndSaveAchievements(self):
        url = self.url_base + self.service_user_stats + self.achievements + self.api_key + \
              self.achievements2 + self.appid
        r = requests.get(url)
        jsondata = json.loads(r.text)

        achievements = jsondata["game"]["availableGameStats"]["achievements"]

        for achievement in achievements:
            a = Achievement(self.id_achievements, achievement["name"], \
                    self.appid, "Garry's Mod", achievement["displayName"], \
                    achievement["description"])
            self.achievement_ids[achievement["name"]] = self.id_achievements
            self.id_achievements += 1
            a.save()


    def getAndSaveOwnedAchievements(self, steamid):
        url = self.url_base + self.service_user_stats + self.ownachievements + \
              self.appid + self.ownachievements2 + self.api_key + \
              self.ownachievements3 + steamid
        r = requests.get(url)
        jsondata = json.loads(r.text)

        own_achs = jsondata["playerstats"].get("achievements")
        if own_achs !=None:
            for own_ach in own_achs:
                achieved = "Achieved"
                if own_ach["achieved"] == 0:
                    achieved = "Not achieved"

                oa = OwnedAchievement(self.id_ownedachievements,steamid, \
                        self.achievement_ids[own_ach["apiname"]], self.steamids[steamid], achieved)
                self.id_ownedachievements += 1
                oa.save()



if __name__ == "__main__":
    steamClient = SteamClient()

    print "Adding DATA to DATABASE - Whole process make take over 30 minutes"
    print "Adding Players - This operation may take some minutes"
    steamClient.getFriends()
    """
    print "Adding Games, and OwnedGames for each Player - This operation may take \
           over 20 minutes"
    for steamid in steamClient.steamids.keys():
        steamClient.getOwnedGames(steamid)
    """
    print "Adding Achievements"
    steamClient.getAndSaveAchievements()

    print "Adding Owned Achievements for each Player - This operation may take \
           over 5 minutes"
    for steamid in steamClient.steamids.keys():
        steamClient.getAndSaveOwnedAchievements(steamid)

