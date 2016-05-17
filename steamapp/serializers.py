from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField,  HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Player,OwnedGame,OwnedAchievement,Game,Achievement

class PlayerSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='steamapp:player-detail')
    ownedgames = HyperlinkedRelatedField(many=True, read_only=True,
    view_name='steamapp:ownedgame-detail')
    ownedachievements = HyperlinkedRelatedField(many=True, read_only=True,
    view_name='steamapp:ownedachievement-detail')
    class Meta:
        model  =  Player
        fields  =  ('uri', 'steamid',  'nickname',  'profileurl',  'privacy',
        'country',  'lastlog', 'ownedgames', 'ownedachievements')

class GameSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='steamapp:game-detail')
    class Meta:
        model  =  Game
        fields  =  ('uri', 'appid', 'name')

class AchievementSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='steamapp:achievement-detail')
    appid = HyperlinkedRelatedField(view_name='steamapp:game-detail', read_only=True)
    class Meta:
        model  =  Achievement
        fields  =  ('uri', 'apiname', 'appid', 'namegame', 'displayname',
        'description')

class OwnedGameSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='steamapp:ownedgame-detail')
    steamid = HyperlinkedRelatedField(view_name='steamapp:player-detail', read_only=True)
    appid = HyperlinkedRelatedField(view_name='steamapp:game-detail', read_only=True)
    class Meta:
        model  =  OwnedGame
        fields  =  ('uri', 'steamid', 'appid', 'nickname', 'gamename',
        'timeplayed_forever')

class OwnedAchievementSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='steamapp:ownedachievement-detail')
    steamid = HyperlinkedRelatedField(view_name='steamapp:player-detail', read_only=True)
    achid = HyperlinkedRelatedField(view_name='steamapp:achievement-detail', read_only=True)
    class Meta:
        model  =  OwnedAchievement
        fields  =  ('uri', 'steamid', 'achid', 'nickname', 'achieved')
