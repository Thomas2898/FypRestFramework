from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from players import views

urlpatterns =[
    path('test/', views.test, name='test'),
    path('players/', views.player_list),
    path('players/<int:pk>', views.player_detail),
    path('players/<str:name>', views.player_detail_name),
    path('teams/', views.team_list),
    path('teams/<int:pk>', views.team_detail),
    path('scores/', views.score_list),
    path('scores/<int:pk>', views.score_detail),
    path('fixtures/', views.fixture_list),
    path('fixtures/<int:pk>', views.fixture_detail),
    path('stats/', views.stat_list),
    path('stats/<int:pk>', views.stat_detail),
    path('PlayerStats/<int:Player_ID>', views.PlayersStats),
]

urlpatterns = format_suffix_patterns(urlpatterns)