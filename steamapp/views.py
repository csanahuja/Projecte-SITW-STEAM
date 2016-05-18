from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateResponseMixin
from django.core.urlresolvers import reverse_lazy

from models import Player, Game, OwnedGame, Achievement, OwnedAchievement
from forms import PlayerForm, GameForm, OwnedGamePlayerForm, OwnedGameGameForm, \
                  AchievementForm, OwnedAchievementPlayerForm, OwnedAchievementAchForm, \
                  AchievementGameForm

from rest_framework import generics,permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from serializers import PlayerSerializer,GameSerializer,\
                        AchievementSerializer,OwnedGameSerializer, \
                        OwnedAchievementSerializer


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


class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj


class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'steamapp/form.html'


class LoginRequiredCheckIsOwnerDeleteView(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    template_name = 'steamapp/delete_form.html'
    success_url = reverse_lazy('player_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
class HomeView(TemplateView):
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)


class PlayerList(ListView, ConnegResponseMixin):
    model = Player
    queryset = Player.objects.filter()
    context_object_name = 'player_list'
    template_name = 'steamapp/player_list.html'


class PlayerDetail(DetailView, ConnegResponseMixin):
    model = Player
    template_name = 'steamapp/player_detail.html'


class PlayerCreate(LoginRequiredMixin, CreateView):
    model = Player
    template_name = 'steamapp/form.html'
    form_class = PlayerForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PlayerCreate, self).form_valid(form)


class GameList(ListView, ConnegResponseMixin):
    model = Game
    queryset = Game.objects.filter()
    context_object_name = 'game_list'
    template_name = 'steamapp/game_list.html'


class GameDetail(DetailView, ConnegResponseMixin):
    model = Game
    template_name = 'steamapp/game_detail.html'


class GameCreate(LoginRequiredMixin, CreateView):
    model = Game
    template_name = 'steamapp/form.html'
    form_class = GameForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(GameCreate, self).form_valid(form)


class OwnedGameDetail(DetailView, ConnegResponseMixin):
    model = OwnedGame
    template_name = 'steamapp/ownedgame_detail.html'


class OwnedGamePlayerCreate(LoginRequiredMixin, CreateView):
    model = OwnedGame
    template_name = 'steamapp/form.html'
    form_class = OwnedGamePlayerForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.steamid = Player.objects.get(steamid=self.kwargs['pk'])
        form.instance.nickname = Player.objects.get(steamid=self.kwargs['pk'])
        return super(OwnedGamePlayerCreate, self).form_valid(form)

class OwnedGameGameCreate(LoginRequiredMixin, CreateView):
    model = OwnedGame
    template_name = 'steamapp/form.html'
    form_class = OwnedGameGameForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.appid = Game.objects.get(appid=self.kwargs['pk'])
        form.instance.gamename = Game.objects.get(appid=self.kwargs['pk'])
        return super(OwnedGameGameCreate, self).form_valid(form)


class AchievementList(ListView, ConnegResponseMixin):
    model = Achievement
    queryset = Achievement.objects.filter()
    context_object_name = 'achievement_list'
    template_name = 'steamapp/achievement_list.html'


class AchievementDetail(DetailView, ConnegResponseMixin):
    model = Achievement
    template_name = 'steamapp/achievement_detail.html'


class AchievementCreate(LoginRequiredMixin, CreateView):
    model = Achievement
    template_name = 'steamapp/form.html'
    form_class = AchievementForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AchievementCreate, self).form_valid(form)

class AchievementGameCreate(LoginRequiredMixin, CreateView):
    model = Achievement
    template_name = 'steamapp/form.html'
    form_class = AchievementGameForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.appid = Game.objects.get(appid=self.kwargs['pk'])
        form.instance.gamename = Game.objects.get(appid=self.kwargs['pk'])
        return super(AchievementGameCreate, self).form_valid(form)


class OwnedAchievementDetail(DetailView, ConnegResponseMixin):
    model = OwnedAchievement
    template_name = 'steamapp/ownach_detail.html'


class OwnAchPlayerCreate(LoginRequiredMixin, CreateView):
    model = OwnedAchievement
    template_name = 'steamapp/form.html'
    form_class = OwnedAchievementPlayerForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.steamid = Player.objects.get(steamid=self.kwargs['pk'])
        form.instance.nickname = Player.objects.get(steamid=self.kwargs['pk'])
        return super(OwnAchPlayerCreate, self).form_valid(form)


class OwnAchAchCreate(LoginRequiredMixin, CreateView):
    model = OwnedAchievement
    template_name = 'steamapp/form.html'
    form_class = OwnedAchievementAchForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.achid = Achievement.objects.get(id=self.kwargs['pk'])
        return super(OwnAchAchCreate, self).form_valid(form)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

class APIPlayerList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Player
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class APIPlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Player
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class APIGameList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Game
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class APIGameDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Game
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class APIAchievementList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Achievement
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class APIAchievementDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Achievement
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class APIOwnedGameDetail(generics.RetrieveUpdateDestroyAPIView):
    model = OwnedGame
    queryset = OwnedGame.objects.all()
    serializer_class = OwnedGameSerializer

class APIOwnedAchievementDetail(generics.RetrieveUpdateDestroyAPIView):
    model = OwnedAchievement
    queryset = OwnedAchievement.objects.all()
    serializer_class = OwnedAchievementSerializer
