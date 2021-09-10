from django.contrib import admin 

# モデルをインポート 
from .models import Profile, Wine, Cart, Topic # 変更（2021/09/10）

# 管理サイトへのモデルの登録 
admin.site.register(Profile) 
admin.site.register(Wine) # 変更(2021/09/07)
admin.site.register(Cart) # 変更(2021/09/08)
admin.site.register(Topic) # 変更(2021/09/10)