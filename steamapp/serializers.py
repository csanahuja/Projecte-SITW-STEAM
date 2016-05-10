from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField,  HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Player,OwnedGame,OwnedAchievement,Game,Ban

class PlayerSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='steamapp:player-detail')
    class Meta:
        model  =  Player
        fields  =  ('uri', 'steamid',  'nickname',  'profileurl',  'privacy',
        'country',  'lastlog')
