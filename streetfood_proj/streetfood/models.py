from django.contrib.auth.models import User # 追加(2021.08.29.0:23)
from django.db import models 
 
GENDER_LIST = ( (0, '男性'), (1, '女性') )
dict_gender_list = dict(GENDER_LIST)

#デフォルトであるdjango.dbのmodelsを継承して作成する
class Profile(models.Model):
    
    #django仕様のメタクラス(クラス自体の設定を記述)(管理画面での表示内容を設定)
    class Meta:
        verbose_name = 'ユーザー情報データ'
        verbose_name_plural = 'ユーザー情報データ'
    #ユーザーの設定。下記のフィールドとの紐づけはビューで行う
    user = models.OneToOneField(User, verbose_name='ユーザー',null=True, blank=True, on_delete=models.CASCADE)

    #フィールドの設定。コード１行がフィールド１列に対応する。
    id = models.CharField(max_length=6,primary_key=True)
    age = models.IntegerField('年齢')
    gender = models.IntegerField('性別',choices=GENDER_LIST)
    pref_name = models.CharField('都道府県',max_length=20)      # '東京都'
    city_name = models.CharField('市区町村',max_length=50)      # '世田谷区'
    district_name = models.CharField('町丁目',max_length=50)    # '喜多見７丁目'
    
    #管理画面で表示される文字列を定義する
    def __str__(self):
#加筆ここから
        user_str = ''
        if self.user is not None:
            user_str = '(' + self.user.username + ')'
#加筆ここまで
        return self.id+' '+str(self.age)+'歳 ' \
            +dict_gender_list.get(self.gender)+' ' \
                +self.pref_name+self.city_name+self.district_name

class Food(models.Model):
    class Meta:
        verbose_name = '商品データ'
        verbose_name_plural = '商品データ'
    
    id = models.CharField('商品ID',max_length=6,primary_key=True) # 'A00001'
    food_name = models.CharField('商品名',max_length=20)
    price = models.FloatField('価格')
    image = models.CharField('画像ファイル',max_length=20)

#加筆ここから
    owner = models.ForeignKey(Profile,
        verbose_name='所有者',
        null=True, blank=True,
        on_delete=models.CASCADE
    )

#加筆ここまで

    def __str__(self):
        return self.id+' '+self.food_name

class Cart(models.Model):
    
    #django仕様のメタクラス(クラス自体の設定を記述)(管理画面での表示内容を設定)
    class Meta:
        verbose_name = 'カート情報'
        verbose_name_plural = 'カート情報'
    #ユーザーID
    user_id = models.CharField(max_length=6)
    #商品ID
    product_id = models.CharField(max_length=6)
    #追加時刻
    timestamp = models.DateTimeField('追加日時', auto_now_add=True)
    # ユーザー住所
    pref_name = models.CharField('都道府県',max_length=20)      # '東京都'
    city_name = models.CharField('市区町村',max_length=50)      # '世田谷区'
    district_name = models.CharField('町丁目',max_length=50)    # '喜多見７丁目'
    #管理画面で表示される文字列を定義する
    def __str__(self):
        return self.user_id + ' ' + self.product_id
