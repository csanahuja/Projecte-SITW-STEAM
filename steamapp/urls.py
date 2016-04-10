from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import RedirectView

from models import Player, Game
from views import PlayerList, PlayerDetail, GameList, GameDetail

urlpatterns = patterns('',
    # Home page
    url(r'^$',
        RedirectView.as_view(url=reverse_lazy('steamapp:player_list', kwargs={'extension': 'html'})),
        name='home_page'),

    # List Players: /steamapp/player.json
    url(r'^players\.(?P<extension>(json|xml|html))$',
        PlayerList.as_view(),
        name='player_list'),

    # Player details, ex.: /steamapps/players/<steamid>.json
    url(r'^players/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        PlayerDetail.as_view(),
        name='player_detail'),

    # List Games: /steamapp/games.json
    url(r'^games\.(?P<extension>(json|xml|html))$',
        GameList.as_view(),
        name='game_list'),

    # Game details, ex.: /steamapps/players/<appid>.json
    url(r'^games/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        GameDetail.as_view(),
        name='game_detail'),

)
