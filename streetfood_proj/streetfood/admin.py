from django.contrib import admin 

# モデルをインポート 
from .models import Profile, Food, Cart

# 管理サイトへのモデルの登録 
admin.site.register(Profile) 
admin.site.register(Food) 
admin.site.register(Cart)