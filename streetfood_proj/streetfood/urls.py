# path()関数のインボート 
from django.urls import path
from . import views
from streetfood.views import concept, food, topic, mypage # 追加(2021.08.29.13:34)


# ルーティングの設定 

app_name = 'streetfood'
#変更！
urlpatterns = [
    path('concept',concept.concept_top, name='concept_top'),

    path('food', food.list_view, name='food_list'),
    path('food/<slug:food_id>', food.detail_view, name='food_detail'),

    path('topic', topic.live_view, name='topic_live'),# 追加(2021.08.29.20:29)

    path('mypage', mypage.mypage_top, name='mypage_top'),# 追加(2021.08.29.16:03)
    path('edit_cart/<slug:food_id>', food.edit_cart, name='edit_cart'), #追加(2021.08.29.16:53)
    ]