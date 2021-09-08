from django.contrib import admin 

# モデルをインポート 
from .models import Profile, Wine, Cart # 変更予定（2021/09/09）

# 管理サイトへのモデルの登録 
admin.site.register(Profile) 
admin.site.register(Wine) # 変更(2021/09/07)
admin.site.register(Cart) # 変更(2021/09/08)