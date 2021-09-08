from django.contrib import admin 

# モデルをインポート 
from .models import Profile, Wine # 変更予定（2021/09/04）

# 管理サイトへのモデルの登録 
admin.site.register(Profile) 
admin.site.register(Wine) # 変更予定（2021/09/04）