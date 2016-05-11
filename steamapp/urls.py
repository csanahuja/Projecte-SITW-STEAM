from django.conf.urls import url
from django.conf import settings
from django.contrib.auth.views import login, logout

from models import Player, Game, OwnedGame
from views import PlayerList, PlayerDetail, GameList, GameDetail, \
                  OwnedGameDetail, BanDetail, AchievementList, \
                  AchievementDetail, OwnedAchievementDetail, HomeView
from views import PlayerCreate, GameCreate, AchievementCreate
from forms import PlayerForm, GameForm, AchievementForm
from views import APIPlayerList,APIPlayerDetail,APIGameList,APIGameDetail, \
                  APIAchievementList,APIAchievementDetail

urlpatterns = [
    # Home page
    url(r'^$',
        HomeView.as_view(template_name='steamapp/home.html'),
        name = 'home'),

    #Login
     url(r'^login/$',
        login,
        name='login'),

    #Logout
    url(r'^logout/$',
        logout,
        name='logout',
        kwargs={'next_page': '/'}),

    # List Players: /steamapp/player.json
    url(r'^players\.(?P<extension>(json|xml|html))?$',
        PlayerList.as_view(),
        name='player_list'),

    # Player details, ex.: /steamapps/players/<steamid>.json
    url(r'^players/(?P<pk>\d+)\.(?P<extension>(json|xml|html))?$',
        PlayerDetail.as_view(),
        name='player_detail'),

    # Create a Player: /steamapp/players/create/
    url(r'^players/create/$',
        PlayerCreate.as_view(),
        name='player_create'),

    # List Games: /steamapp/games.json
    url(r'^games\.(?P<extension>(json|xml|html))?',
        GameList.as_view(),
        name='game_list'),

    # Game details, ex.: /steamapps/players/<appid>.json
    url(r'^games/(?P<pk>\d+)\.(?P<extension>(json|xml|html))?$',
        GameDetail.as_view(),
        name='game_detail'),

    # Create a Game: /steamapp/games/create/
    url(r'^games/create/$',
        GameCreate.as_view(),
        name='game_create'),

    # Owned games details, ex.:  /steamapps/ownedgames/<id>.json
    url(r'^ownedgames/(?P<pk>\d+)\.(?P<extension>(json|xml|html))?$',
        OwnedGameDetail.as_view(),
        name='ownedgame_detail'),

    # Ban details, ex.:  /steamapps/players/<steamid>/baninfo.json
    url(r'^banstatus/(?P<pk>\d+)\.(?P<extension>(json|xml|html))?$',
        BanDetail.as_view(),
        name='ban_detail'),

    # List Achievements: /steamapp/achievements.json
    url(r'^achievements\.(?P<extension>(json|xml|html))?',
        AchievementList.as_view(),
        name='achievement_list'),

    # Achievements details, ex.: /steamapps/achievements/<id>.json
    url(r'^achievements/(?P<pk>\d+)\.(?P<extension>(json|xml|html))?$',
        AchievementDetail.as_view(),
        name='achievement_detail'),

    # Create a Game: /steamapp/achievements/create/
    url(r'^achievements/create/$',
        AchievementCreate.as_view(),
        name='achievement_create'),

    # Owned Achievements details, ex.:  /steamapps/ownedachievements/<id>.json
    url(r'^ownedachievements/(?P<pk>\d+)\.(?P<extension>(json|xml|html))?$',
        OwnedAchievementDetail.as_view(),
        name='ownach_detail'),
        
    # API patterns
    url(r'^api/players/$',  APIPlayerList.as_view(),  name='player-list'),
    url(r'^api/players/(?P<pk>\d+)/$',
            APIPlayerDetail.as_view(), name='player-detail'),
    url(r'^api/games/$',  APIGameList.as_view(),  name='game-list'),
    url(r'^api/games/(?P<pk>\d+)/$',
            APIGameDetail.as_view(), name='game-detail'),
    url(r'^api/achievements/$',
            APIAchievementList.as_view(),  name='achievement-list'),
    url(r'^api/achievements/(?P<pk>\d+)/$',
            APIAchievementDetail.as_view(), name='achievement-detail'),

]
