from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField,  HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Player,OwnedGame,OwnedAchievement,Game,Ban,Achievement

class PlayerSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='steamapp:player-detail')
    class Meta:
        model  =  Player
        fields  =  ('uri', 'steamid',  'nickname',  'profileurl',  'privacy',
        'country',  'lastlog')

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
