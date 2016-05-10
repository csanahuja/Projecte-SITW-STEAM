from django.forms import ModelForm
from models import Player, Game, Achievement

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
