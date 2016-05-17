from django.forms import ModelForm
from models import Player, Game, Achievement, OwnedGame

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        exclude = ('user',)

class GameForm(ModelForm):
    class Meta:
        model = Game
        exclude = ('user',)

class AchievementForm(ModelForm):
    class Meta:
        model = Achievement
        exclude = ('user',)

class OwnedGameForm(ModelForm):
    class Meta:
        model = OwnedGame
        exclude = ('user',)
