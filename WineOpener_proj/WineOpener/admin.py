from django.contrib import admin 

# モデルをインポート 
from .models import Profile, RentRoom # 変更予定（2021/09/04）

# 管理サイトへのモデルの登録 
admin.site.register(Profile) 
admin.site.register(RentRoom) # 変更予定（2021/09/04）