from django.contrib import admin 

# モデルをインポート 
from .models import Profile, Food

# 管理サイトへのモデルの登録 
admin.site.register(Profile) 
admin.site.register(Food) 