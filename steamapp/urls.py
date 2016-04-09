from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import RedirectView

from models import Player
#from forms import RestaurantForm, DishForm
from views import PlayerList, PlayerDetail

urlpatterns = patterns('',
    # Home page
    url(r'^$',
        RedirectView.as_view(url=reverse_lazy('steamapp:player_list', kwargs={'extension': 'html'})),
        name='home_page'),

    # List Players: /steamapp/player.json
    url(r'^players\.(?P<extension>(json|xml|html))$',
        PlayerList.as_view(),
        name='player_list'),

    # Player details, ex.: /steamapps/players/1.json
    url(r'^players/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        PlayerDetail.as_view(),
        name='player_detail'),

)
