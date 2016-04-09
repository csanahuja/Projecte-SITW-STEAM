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
    steamid = models.ForeignKey(Player, null = True, related_name='ownedgames')
    appid = models.ForeignKey(Game, null = True, related_name='ownedgames')
    nickname = models.TextField(blank=True, null=True)
    gamename = models.TextField(blank=True, null=True)
    timeplayed_forever = models.IntegerField(default=0)

    class Meta:
        unique_together = (('steamid', 'appid'),)

    def __unicode__(self):
        return "Player: "+ self.nickname + " Game: " + self.gamename


class Achievement(models.Model):
    apiname = models.TextField(primary_key=True)
    appid = models.ForeignKey(Game, related_name='achievements')
    namegame = models.TextField(blank=True, null=True)
    displayname = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return "Game: " + self.namegame + " - Achievement: " + self.displayname


class OwnedAchievement(models.Model):
    steamid = models.ForeignKey(Player, related_name='achievements_owned')
    appid = models.ForeignKey(Game, related_name='achievements_owned')
    apiname = models.ForeignKey(Achievement, related_name='achievements_owned')
    nickname = models.TextField(blank=True, null=True)
    gamename = models.TextField(blank=True, null=True)
    achieved = models.TextField(default='No')

    class Meta:
        unique_together = (('steamid', 'apiname'),)

    def __unicode__(self):
        return "Player: " + self.nickname + " - " + str(self.apiname) \
               + " - State: " + self.achieved


class Ban(models.Model):
    steamid = models.ForeignKey(Player, related_name='bans')
    communityBanned = models.BooleanField(default=False)
    VACBanned = models.BooleanField(default=False)
    numberOfVACBans = models.IntegerField(default=0)
    daysSinceLastBan = models.IntegerField(default=0)

    def __unicode__(self):
        return "Player: " + self.steamid
