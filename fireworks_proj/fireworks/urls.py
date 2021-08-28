# path()関数のインボート(2021.08.27.17:54)
from django.urls import path
from . import views 
from fireworks.views import fireworks #追加(2021.08.28.10:28)
# ルーティングの設定 

app_name = 'fireworks' #追加(2021.08.28.10:36)

urlpatterns = [ 
    path('fireworks', fireworks.list_view, name='fireworks_list'),
    path('fireworks/<slug:fireworks_id>', fireworks.detail_view, name='fireworks_detail'), # 追加(2021.08.28.18:34)
]