from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from streetfood.models import GENDER_LIST, Profile

class RegisterForm(UserCreationForm):
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER_LIST, required=True)
    pref_name = forms.CharField(required=True)      # '東京都'
    city_name = forms.CharField(required=True)      # '世田谷区'
    district_name = forms.CharField(required=True)    # '喜多見７丁目'

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','age','gender','pref_name','city_name','district_name']
        labels = {
            'username': 'ユーザー名',
            'password1': 'パスワード',
            'password2': 'パスワード確認',
            'age': '年齢',
            'gender': '性別',
            'pref_name': '都道府県',
            'city_name': '市区',
            'district_name': '町村',
        }

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError('Cannot create User and Profile without database save')
        
        user = super().save()

        try:
            max_id = Profile.objects.latest('id').id
        except ObjectDoesNotExist:
            max_id = 'B00000'

        prof_id = 'B'+(str(int(max_id[1:])+1).zfill(5))

        age = self.cleaned_data['age']
        gender = self.cleaned_data['gender']
        pref_name = self.cleaned_data['pref_name']      # '東京都'
        city_name = self.cleaned_data['city_name']      # '世田谷区'
        district_name = self.cleaned_data['district_name']    # '喜多見７丁目'
        
        profile = Profile(id=prof_id,age=age,gender=gender,pref_name=pref_name,city_name=city_name,district_name=district_name,user_id=user.id)
        profile.save()

        return user