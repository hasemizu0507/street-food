from django.contrib.auth.models import User # 追加(2021.08.28.10:48)
from django.db import models 
 
GENDER_LIST = ( (0, '男性'), (1, '女性') )
dict_gender_list = {0:'男性',1:'女性'}

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
    
    #管理画面で表示される文字列を定義する
    def __str__(self):
        return self.id+' '+str(self.age)+'歳 ' \
            +dict_gender_list.get(self.gender)+' ' \
            #+str(self.household_num)+'人世帯 ' 

class Fireworks(models.Model):
    class Meta:
        verbose_name = '販売花火データ'
        verbose_name_plural = '販売花火データ'
    
    id = models.CharField('花火ID',max_length=6,primary_key=True) # 'A00001'
    fireworks_type = models.CharField('花火タイプ',max_length=50)      # '手持ち花火'，'打上花火'，'噴出花火'，'ロケット花火'，'おもしろ花火'，'セット花火'
    price = models.IntegerField('値段')
    contents = models.IntegerField('内容量') # '10本入'

    def __str__(self):
        return self.id