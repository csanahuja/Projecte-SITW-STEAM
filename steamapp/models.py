from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

class Player(models.Model):
    steamid = models.TextField(primary_key=True)
    nickname = models.TextField()
    profileurl = models.TextField()
    privacity = models.TextField(blank=True, null=True)
    currentstate = models.TextField(blank=True, null=True)
    lastlog = models.DateField(null=True)


class Game(models.Model):
    appid = models.TextField(primary_key=True)
    name = models.TextField()


class GameOwned(models.Model):
    steamid = models.ForeignKey(Player, related_name='games_owned')
    appid = models.ForeignKey(Game, related_name='games_owned')
    timeplayed_forever = models.IntegerField(default=0)
    timeplayed_lastweek = models.IntegerField(default=0)

class Achievement(models.Model):
    apiname = models.TextField(primary_key=True)
    appid = models.ForeignKey(Game, related_name='achievements')
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class AchievementOwned(models.Model):
    steamid = models.ForeignKey(Player, related_name='achievements_owned')
    apiname = models.ForeignKey(Achievement, related_name='achievements_owned')
    achieved = models.TextField(default='No')

class Ban(models.Model):
    steamid = models.ForeignKey(Player, related_name='bans')
    communityBanned = models.BooleanField(default=False)
    VACBanned = models.BooleanField(default=False)
    numberOfVACBans = models.IntegerField(default=0)
    daysSinceLastBan = models.IntegerField(default=0)
