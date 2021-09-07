from django.contrib import admin 

# モデルをインポート 
from .models import Profile, wine, Cart

# 管理サイトへのモデルの登録 
admin.site.register(Profile) 
admin.site.register(wine) 
admin.site.register(Cart) 
