from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from datetime import date



class Player(models.Model):
    steamid = models.TextField(primary_key=True)
    nickname = models.TextField()
    profileurl = models.TextField()
    privacy = models.TextField(default="private")
    country = models.TextField(blank=True, null=True)
    lastlog = models.IntegerField(default=0)

    def __unicode__(self):
        return self.nickname


class Game(models.Model):
    appid = models.TextField(primary_key=True)
    name = models.TextField()

    def __unicode__(self):
        return self.name


class OwnedGame(models.Model):
    steamid = models.ForeignKey(Player, related_name='games_owned')
    appid = models.ForeignKey(Game, related_name='games_owned')
    timeplayed_forever = models.IntegerField(default=0)
    timeplayed_lastweek = models.IntegerField(default=0)

    def __unicode__(self):
        return "Player: "+ self.steamid + " Game: " + self.appid


class Achievement(models.Model):
    apiname = models.TextField(primary_key=True)
    appid = models.ForeignKey(Game, related_name='achievements')
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return "Achievement: " + self.apiname + " Game: " + Game.appid


class OwnedAchivement(models.Model):
    steamid = models.ForeignKey(Player, related_name='achievements_owned')
    apiname = models.ForeignKey(Achievement, related_name='achievements_owned')
    achieved = models.TextField(default='No')

    def __unicode__(self):
        return "Player: " + self.steamdid + " Achievement: " + self.apiname


class Ban(models.Model):
    steamid = models.ForeignKey(Player, related_name='bans')
    communityBanned = models.BooleanField(default=False)
    VACBanned = models.BooleanField(default=False)
    numberOfVACBans = models.IntegerField(default=0)
    daysSinceLastBan = models.IntegerField(default=0)

    def __unicode__(self):
        return "Player: " + self.steamid
