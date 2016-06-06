from django.forms import ModelForm
from models import Player, Game, Achievement, OwnedGame, OwnedAchievement, GameReview

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        exclude = ('user',)

class GameForm(ModelForm):
    class Meta:
        model = Game
        exclude = ('user',)

class GameReviewForm(ModelForm):
    class Meta:
        model = GameReview
        exclude = ('user','date','game',)

class AchievementForm(ModelForm):
    class Meta:
        model = Achievement
        exclude = ('user',)

class AchievementGameForm(ModelForm):
    class Meta:
        model = Achievement
        exclude = ('user','appid','gamename',)

class OwnedGameForm(ModelForm):
    class Meta:
        model = OwnedGame
        exclude = ('user',)

class OwnedGamePlayerForm(ModelForm):
    class Meta:
        model = OwnedGame
        exclude = ('user','steamid','nickname',)

class OwnedGameGameForm(ModelForm):
    class Meta:
        model = OwnedGame
        exclude = ('user','appid','gamename',)

class OwnedAchievementForm(ModelForm):
    class Meta:
        model = OwnedAchievement
        exclude = ('user',)

class OwnedAchievementPlayerForm(ModelForm):
    class Meta:
        model = OwnedAchievement
        exclude = ('user','steamid','nickname')

class OwnedAchievementAchForm(ModelForm):
    class Meta:
        model = OwnedAchievement
        exclude = ('user','achid',)
