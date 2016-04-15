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

    def get_absolute_url(self):
        return reverse('steamapp:player_detail', kwargs={'pk': self.pk})


class Game(models.Model):
    appid = models.TextField(primary_key=True)
    name = models.TextField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('steamapp:game_detail', kwargs={'pk': self.pk})


class OwnedGame(models.Model):
    steamid = models.ForeignKey(Player, null = True, related_name='ownedgames')
    appid = models.ForeignKey(Game, null = True, related_name='gamesownedby')
    nickname = models.TextField(blank=True, null=True)
    gamename = models.TextField(blank=True, null=True)
    timeplayed_forever = models.IntegerField(default=0)

    class Meta:
        unique_together = (('steamid', 'appid'),)

    def __unicode__(self):
        return "Player: "+ self.nickname + " Game: " + self.gamename

    def get_absolute_url(self):
        return reverse('steamapp:owned_detail', kwargs={'pk': self.pk})


class Achievement(models.Model):
    apiname = models.TextField(blank=True, null=True)
    appid = models.ForeignKey(Game, related_name='achievements')
    namegame = models.TextField(blank=True, null=True)
    displayname = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return "Game: " + self.namegame + " - Achievement: " + self.displayname

    def get_absolute_url(self):
        return reverse('steamapp:achievement_detail', kwargs={'pk': self.pk})


class OwnedAchievement(models.Model):
    steamid = models.ForeignKey(Player, related_name='ownedachievements')
    achid = models.ForeignKey(Achievement, related_name='achievementsownedby')
    nickname = models.TextField(blank=True, null=True)
    achieved = models.TextField(default='No')

    class Meta:
        unique_together = (('steamid', 'achid'),)

    def __unicode__(self):
        return "Player: " + self.nickname + " - " + str(self.achid.displayname) \
               + " - State: " + self.achieved

    def get_absolute_url(self):
        return reverse('steamapp:ownach_detail', kwargs={'pk': self.pk})


class Ban(models.Model):
    steamid = models.ForeignKey(Player, related_name='bans')
    nickname = models.TextField(blank=True, null=True)
    communityBanned = models.BooleanField(default=False)
    VACBanned = models.BooleanField(default=False)
    numberOfVACBans = models.IntegerField(default=0)
    daysSinceLastBan = models.IntegerField(default=0)

    def __unicode__(self):
        return "Player: " + self.nickname + " - Number of VAC Bans: " + \
                str(self.numberOfVACBans)

    def get_absolute_url(self):
        return reverse('steamapp:ban_detail', kwargs={'pkp': self.steamid.pk, \
                        'pk': self.pk})
