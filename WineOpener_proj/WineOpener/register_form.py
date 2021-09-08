from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from WineOpener.models import GENDER_LIST, Profile

class RegisterForm(UserCreationForm):
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER_LIST, required=True)
    mobile = forms.CharField(required=True)
    email = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','age','gender', 'mobile', 'email']
        labels = {
            'username': 'ユーザー名',
            'password1': 'パスワード',
            'password2': 'パスワード確認',
            'age': '年齢',
            'gender': '性別',
            'mobile': '携帯番号',
            'email': 'メールアドレス'
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
        mobile = self.cleaned_data['mobile']
        email = self.cleaned_data['email']

        profile = Profile(id=prof_id,age=age,gender=gender,mobile=mobile,email=email,user_id=user.id)
        profile.save()

        return user