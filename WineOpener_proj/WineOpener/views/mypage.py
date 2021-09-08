from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import json
from WineOpener.models import Profile, Wine, Cart

# 以下4つ追加（決済用）(2021/09/09)
from django.conf import settings
import json
import stripe
from django.urls import reverse

@login_required
def mypage_top(request):
    user = request.user
    profile = user.profile
    user_id = user.id # 追加(2021/09/08)
    products = Cart.objects.filter(user_id=user_id) # 追加(2021/09/08)
    return render(request, 'WineOpener/mypage.html', {'profile':profile,'products':products}) #'assessments':myassessments

# 決済成功時の関数　追加(2021/09/09)
def success(request):
    # テンプレートを表示するだけ
    return render(request, 'WineOpener/success.html') 

# 決済中止時の関数
def cancel(request):
    # テンプレートを表示するだけ
    return render(request, 'WineOpener/cancel.html') 

# 決済内容確認時の関数
def checkout(request):
    # settings.pyから読み込んだ公開鍵をjson形式にしてテンプレートcheckout.htmlに渡す
    key_data = {
        "publishable_key":settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render(request, 'WineOpener/checkout.html', {'data_json':json.dumps(key_data)})
# 「この商品を購入」ボタンが押された時の関数
def create_checkout_session(request):
    # settings.pyから秘密鍵を読み込む
   stripe.api_key = settings.STRIPE_SECRET_KEY

   try:
       checkout_session = stripe.checkout.Session.create(
           # カード決済
           payment_method_types=['card'],
           # 決済内容を記述
           line_items=[
               {
                   'price_data': {
                       # 通貨（円）
                       'currency': 'jpy',
                       # 金額
                       'unit_amount': 2000,
                       # 商品説明・画像
                       'product_data': {
                           'name': 'sample house',
                           'images': ['http://gahag.net/img/201606/12s/gahag-0095672681-1.jpg'],
                       },
                   },
                   # 個数
                   'quantity': 1,
               },
           ],
           mode='payment',
           # 成功すれば"success"へ
           success_url=request.build_absolute_uri(reverse('WineOpener:success')),
           # 中止すれば"cancel"へ
           cancel_url=request.build_absolute_uri(reverse('WineOpener:cancel')),
       )

       print(checkout_session.id)
       return JsonResponse({'id': checkout_session.id})
   except Exception as e:
       return JsonResponse({'error':str(e)})