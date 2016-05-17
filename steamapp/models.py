from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Player(models.Model):
    steamid = models.TextField(primary_key=True)
    nickname = models.TextField()
    profileurl = models.TextField()
    privacy = models.TextField(default="private")
    country = models.TextField(blank=True, null=True)
    lastlog = models.IntegerField(default=0)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return str(self.nickname)

    def get_absolute_url(self):
        return reverse('steamapp:player_detail', kwargs={'pk': self.pk})


class Game(models.Model):
    appid = models.TextField(primary_key=True)
    name = models.TextField()
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('steamapp:game_detail', kwargs={'pk': self.pk})


class OwnedGame(models.Model):
    steamid = models.ForeignKey(Player, null = True, related_name='ownedgames')
    appid = models.ForeignKey(Game, null = True, related_name='gamesownedby')
    nickname = models.TextField(blank=True, null=True)
    gamename = models.TextField(blank=True, null=True)
    timeplayed_forever = models.IntegerField(default=0)
    user = models.ForeignKey(User, default=1)

    class Meta:
        unique_together = (('steamid', 'appid'),)

    def __unicode__(self):
        return "Player: "+ str(self.nickname) + " Game: " + str(self.gamename)

    def get_absolute_url(self):
        return reverse('steamapp:ownedgame_detail', kwargs={'pk': self.pk})


class Achievement(models.Model):
    apiname = models.TextField(blank=True, null=True)
    appid = models.ForeignKey(Game, related_name='achievements')
    gamename = models.TextField(blank=True, null=True)
    displayname = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return "Game: " + str(self.gamename) + " - Achievement: " + str(self.displayname)

    def get_absolute_url(self):
        return reverse('steamapp:achievement_detail', kwargs={'pk': self.pk})


class OwnedAchievement(models.Model):
    steamid = models.ForeignKey(Player, related_name='ownedachievements')
    achid = models.ForeignKey(Achievement, related_name='achievementsownedby')
    nickname = models.TextField(blank=True, null=True)
    achieved = models.TextField(default='No')
    user = models.ForeignKey(User, default=1)

    class Meta:
        unique_together = (('steamid', 'achid'),)

    def __unicode__(self):
        return "Player: " + str(self.nickname) + " - " + str(self.achid.displayname) \
               + " - State: " + str(self.achieved)

    def get_absolute_url(self):
        return reverse('steamapp:ownedachievement_detail', kwargs={'pk': self.pk})
