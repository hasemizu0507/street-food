# path()関数のインボート 
from django.urls import path
from WineOpener.views import live, readme, mypage
# ルーティングの設定

app_name = 'WineOpener'

urlpatterns = [ 
    path('readme', readme.readme_view, name='readme'), 
    
    path('live', live.list_view, name='live_list'),
    path('live/live1', live.detail_view, name='live_detail'),
    path('live/live1/<slug:livewine_id>', live.wine_view, name='live_wine'),

    path('mypage', mypage.mypage_top, name='mypage_top'),
    path('edit_cart/<slug:livewine_id>', live.edit_cart, name='edit_cart'), # 追加(2021/09/08)
]