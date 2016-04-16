from django.conf.urls import patterns, url
from models import Player, Game, OwnedGame
from views import PlayerList, PlayerDetail, GameList, GameDetail, \
                  OwnedGameDetail, BanDetail, AchievementList, \
                  AchievementDetail, OwnedAchievementDetail

urlpatterns = patterns('',
    # Home page
    url(r'^$',
        'steamapp.views.home'),

    #Login
     url(r'^login/$',
        'django.contrib.auth.views.login',
        name='login',),

    #Logout
    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout',
        kwargs={'next_page': '/'}),

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

    # Owned games details, ex.:  /steamapps/ownedgames/<id>.json
    url(r'^ownedgames/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        OwnedGameDetail.as_view(),
        name='ownedgame_detail'),

    # Ban details, ex.:  /steamapps/players/<steamid>/baninfo.json
    url(r'^banstatus/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        BanDetail.as_view(),
        name='ban_detail'),

    # List Achievements: /steamapp/achievements.json
    url(r'^achievements\.(?P<extension>(json|xml|html))$',
        AchievementList.as_view(),
        name='achievement_list'),

    # Achievements details, ex.: /steamapps/achievements/<id>.json
    url(r'^achievements/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        AchievementDetail.as_view(),
        name='achievement_detail'),

    # Owned Achievements details, ex.:  /steamapps/ownedachievements/<id>.json
    url(r'^ownedachievements/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        OwnedAchievementDetail.as_view(),
        name='ownach_detail'),

)
