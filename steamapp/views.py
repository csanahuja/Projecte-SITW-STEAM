from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateResponseMixin
from models import Player, Game, OwnedGame, Ban, Achievement, OwnedAchievement


class ConnegResponseMixin(TemplateResponseMixin):

    def render_json_object_response(self, objects, **kwargs):
        json_data = serializers.serialize(u"json", objects, **kwargs)
        return HttpResponse(json_data, content_type=u"application/json")

    def render_xml_object_response(self, objects, **kwargs):
        xml_data = serializers.serialize(u"xml", objects, **kwargs)
        return HttpResponse(xml_data, content_type=u"application/xml")

    def render_to_response(self, context, **kwargs):
        if 'extension' in self.kwargs:
            try:
                objects = [self.object]
            except AttributeError:
                objects = self.object_list
            if self.kwargs['extension'] == 'json':
                return self.render_json_object_response(objects=objects)
            elif self.kwargs['extension'] == 'xml':
                return self.render_xml_object_response(objects=objects)
        return super(ConnegResponseMixin, self).render_to_response(context)


def home(request):
    return render_to_response('steamapp/home.html')

class PlayerList(ListView, ConnegResponseMixin):
    model = Player
    queryset = Player.objects.filter()
    context_object_name = 'player_list'
    template_name = 'steamapp/player_list.html'


class PlayerDetail(DetailView, ConnegResponseMixin):
    model = Player
    template_name = 'steamapp/player_detail.html'


class GameList(ListView, ConnegResponseMixin):
    model = Game
    queryset = Game.objects.filter()
    context_object_name = 'game_list'
    template_name = 'steamapp/game_list.html'


class GameDetail(DetailView, ConnegResponseMixin):
    model = Game
    template_name = 'steamapp/game_detail.html'


class OwnedGameDetail(DetailView, ConnegResponseMixin):
    model = OwnedGame
    template_name = 'steamapp/ownedgame_detail.html'


class BanDetail(DetailView, ConnegResponseMixin):
    model = Ban
    template_name = 'steamapp/ban_detail.html'


class AchievementList(ListView, ConnegResponseMixin):
    model = Achievement
    queryset = Achievement.objects.filter()
    context_object_name = 'achievement_list'
    template_name = 'steamapp/achievement_list.html'


class AchievementDetail(DetailView, ConnegResponseMixin):
    model = Achievement
    template_name = 'steamapp/achievement_detail.html'


class OwnedAchievementDetail(DetailView, ConnegResponseMixin):
    model = OwnedAchievement
    template_name = 'steamapp/ownach_detail.html'
