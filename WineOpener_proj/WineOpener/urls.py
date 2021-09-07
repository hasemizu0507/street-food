# path()関数のインボート 
from django.urls import path
from WineOpener.views import live, readme
# ルーティングの設定

app_name = 'WineOpener'

urlpatterns = [ 
    path('readme', readme.readme_view, name='readme'), 
    
    path('live', live.list_view, name='live_list'),
    path('live/live1', live.detail_view, name='live_detail'),
]