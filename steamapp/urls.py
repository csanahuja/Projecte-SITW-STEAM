from django.conf.urls import url
from django.conf import settings
from django.contrib.auth.views import login, logout
from rest_framework.urlpatterns import format_suffix_patterns

from views import PlayerList, PlayerDetail, GameList, GameDetail, \
                  OwnedGameDetail, AchievementList, \
                  AchievementDetail, OwnedAchievementDetail, HomeView

from views import PlayerCreate, GameCreate, OwnedGamePlayerCreate, OwnedGameGameCreate, \
                  AchievementCreate, OwnAchPlayerCreate, OwnAchAchCreate, AchievementGameCreate

from views import APIPlayerList,APIPlayerDetail,APIGameList,APIGameDetail, \
                  APIAchievementList,APIAchievementDetail,APIOwnedGameDetail,\
                  APIOwnedAchievementDetail

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
    url(r'^players(\.(?P<extension>(json|xml)))?$',
        PlayerList.as_view(),
        name='player_list'),

    # Player details, ex.: /steamapps/players/<steamid>.json
    url(r'^players/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',
        PlayerDetail.as_view(),
        name='player_detail'),

    # Create a Player: /steamapp/players/create/
    url(r'^players/create/$',
        PlayerCreate.as_view(),
        name='player_create'),

    # List Games: /steamapp/games.json
    url(r'^games(\.(?P<extension>(json|xml)))?$',
        GameList.as_view(),
        name='game_list'),

    # Game details, ex.: /steamapps/players/<appid>.json
    url(r'^games/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',
        GameDetail.as_view(),
        name='game_detail'),

    # Create a Game: /steamapp/games/create/
    url(r'^games/create/$',
        GameCreate.as_view(),
        name='game_create'),

    # Owned games details, ex.:  /steamapps/ownedgames/<id>.json
    url(r'^ownedgames/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',
        OwnedGameDetail.as_view(),
        name='ownedgame_detail'),

    # Create a OwnedGame: /steamapp/ownedgames/player/create/
    # From a Player
    url(r'^ownedgames/player/create/(?P<pk>\d+)$',
        OwnedGamePlayerCreate.as_view(),
        name='ownedgameplayer_create'),

    # Create a OwnedGame: /steamapp/ownedgames/game/create/
    # From a Game
    url(r'^ownedgames/game/create/(?P<pk>\d+)$',
        OwnedGameGameCreate.as_view(),
        name='ownedgamegame_create'),

    # List Achievements: /steamapp/achievements.json
    url(r'^achievements(\.(?P<extension>(json|xml)))?$',
        AchievementList.as_view(),
        name='achievement_list'),

    # Achievements details, ex.: /steamapps/achievements/<id>.json
    url(r'^achievements/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',
        AchievementDetail.as_view(),
        name='achievement_detail'),

    # Create a Achievement: /steamapp/achievements/create/
    url(r'^achievements/create/$',
        AchievementCreate.as_view(),
        name='achievement_create'),

    # Create a Achievement: /steamapp/achievements/game/create/
    # From a Game
    url(r'^achievements/game/create/(?P<pk>\d+)$',
        AchievementGameCreate.as_view(),
        name='achievementgame_create'),

    # Owned Achievements details, ex.:  /steamapps/ownedachievements/<id>.json
    url(r'^ownedachievements/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',
        OwnedAchievementDetail.as_view(),
        name='ownedachievement_detail'),

    # Create a OwnedAchievement: /steamapp/ownedachievements/player/create/
    # From a Player
    url(r'^ownedachievements/player/create/(?P<pk>\d+)$',
        OwnAchPlayerCreate.as_view(),
        name='ownedachievementplayer_create'),

    # Create a OwnedAchievement: /steamapp/ownedachievements/achievement/create/
    # From a Achievement
    url(r'^ownedachievements/achievement/create/(?P<pk>\d+)$',
        OwnAchAchCreate.as_view(),
        name='ownedachievementach_create'),


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
    url(r'^api/ownedgames/(?P<pk>\d+)/$',
            APIOwnedGameDetail.as_view(), name='ownedgame-detail'),
    url(r'^api/ownedachievements/(?P<pk>\d+)/$',
            APIOwnedAchievementDetail.as_view(), name='ownedachievement-detail'),
]

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api','json', 'xml'])
