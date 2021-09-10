from django.contrib.auth.models import User 
from django.db import models
 
GENDER_LIST = ( (0, '男性'), (1, '女性') )
dict_gender_list = dict(GENDER_LIST) #追加(2021/09/06)

#デフォルトであるdjango.dbのmodelsを継承して作成する
class Profile(models.Model):
    
    #django仕様のメタクラス(クラス自体の設定を記述)(管理画面での表示内容を設定)
    class Meta:
        verbose_name = 'ユーザー情報データ'
        verbose_name_plural = 'ユーザー情報データ'
    #ユーザーの設定。下記のフィールドとの紐づけはビューで行う
    user = models.OneToOneField(User, verbose_name='ユーザー',null=True, blank=True, on_delete=models.CASCADE)

    #フィールドの設定。コード１行がフィールド１列に対応する。
    id = models.CharField(max_length=6,primary_key=True) # 変更（2021/09/07）
    age = models.IntegerField('年齢')
    gender = models.IntegerField('性別',choices=GENDER_LIST)
    mobile = models.CharField('電話番号',max_length=12)
    email = models.CharField('メールアドレス',max_length=100)
    
    
    #管理画面で表示される文字列を定義する # 変更（2021/09/04）
    def __str__(self):
        user_str = ''
        if self.user is not None:
            user_str = '(' + self.user.username + ')'
        return self.id+' '\
            +str(self.age)+'歳 ' \
            +dict_gender_list.get(self.gender)+' ' \
            +str(self.mobile)+' ' \
            +str(self.email)+' '\
            +user_str

class Wine(models.Model): # 変更(2021/09/08)
    class Meta:
        verbose_name = '販売ワインデータ'
        verbose_name_plural = '販売ワインデータ'
    
    id = models.CharField('ワインID',max_length=6,primary_key=True) # 'A00001' # 変更（2021/09/07）
    thumbnail = models.CharField('サムネイル',max_length=50)      # 'WineOpener/images/live1.jpg'
    name = models.CharField('ワイン名',max_length=50)      # 'シャトー・オー・プニャン'
    price = models.IntegerField('価格')    # '2200'
    stock = models.IntegerField('在庫')    # '5'
    harvest_year = models.IntegerField('収穫年')       # '2018'
    producer = models.CharField('生産者',max_length=50)
    region = models.CharField('産地',max_length=50)
    style = models.CharField('タイプ',max_length=20)        # '赤ワイン', '白ワイン' など
    type = models.CharField('品種',max_length=50)

    owner = models.ForeignKey(Profile, # 変更予定(2021/09/08)
        verbose_name='所有者',
        null=True, blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.id+' '\
            +self.thumbnail+' ' \
            +self.name+' ' \
            +str(self.price)+' ' \
            +str(self.stock)+' ' \
            +str(self.harvest_year)+' '\
            +self.producer+' '\
            +self.region+' '\
            +self.style+' '\
            +self.type

class Cart(models.Model): #変更(2021/09/08)
    class Meta:
        verbose_name = 'カート情報'
        verbose_name_plural = 'カート情報'
    
    user_id = models.CharField('ユーザーID',max_length=6) # ユーザーID
    product_id = models.CharField('商品ID',max_length=6) # 商品ID
    timestamp = models.DateTimeField('追加日時',auto_now_add=True) # 追加日時

    def __str__(self):
        return self.user_id +' '\
            +self.product_id +' '\
            +self.timestamp

class Topic(models.Model):
    class Meta:
        managed = True
        verbose_name = 'コメント'
        verbose_name_plural = 'コメント'
        db_table = "topic"
    
    user_id = models.CharField('ユーザーID',max_length=6) # ユーザーID
    stream_id = models.CharField('コメントID',max_length=6) # コメントID
    comment = models.CharField('コメント', max_length=50) # コメント
    timestamp = models.DateTimeField('追加日時', auto_now_add=True) # 追加日時
    def __str__(self):
        return self.user_id + ' '\
            + self.stream_id + ' '\
            + self.comment + ' '\
            + str(self.timestamp)