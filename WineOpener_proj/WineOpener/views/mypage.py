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
from django.db.models import Sum

@login_required
def mypage_top(request):
    user = request.user
    profile = user.profile
    user_id = user.id # 追加(2021/09/08)
    products = Cart.objects.filter(user_id=user_id) # ユーザーIDがログイン中しているユーザのIDになっているproductsを取り出す 追加(2021/09/08)
    return render(request, 'WineOpener/mypage.html', {'profile':profile,'products':products}) #'assessments':myassessments

def success(request): # 決済成功時の関数　追加(2021/09/09)
    return render(request, 'WineOpener/success.html') # テンプレートを表示するだけ


def cancel(request): # 決済中止時の関数
    return render(request, 'WineOpener/cancel.html') # テンプレートを表示するだけ


def checkout(request): # 決済内容確認時の関数
    key_data = {
        "publishable_key":settings.STRIPE_PUBLISHABLE_KEY, # settings.pyから読み込んだ公開鍵をjson形式にしてテンプレートcheckout.htmlに渡す
    }

    user = request.user
    user_id = user.id
    user_name = user.username
    product_id = Cart.objects.filter(user_id=user_id).values_list('product_id', flat=True) # ユーザーIDがログインしているユーザのIDになっている"products"を取り出す 追加(2021/09/09)
    products = Wine.objects.filter(id__in=product_id).values('id', 'name', 'price')
    price_total = Wine.objects.filter(id__in=product_id).aggregate(Sum('price'))['price__sum']
    price_total = round(price_total)

    return render(request, 'WineOpener/checkout.html', {'data_json':json.dumps(key_data), "products":products, "price":price_total, "user_id":user_name}) # 追加(2021/09/09)「"user_id":user_name」の箇所合ってる？？

def create_checkout_session(request):# 「この商品を購入」ボタンが押された時の関数 
    stripe.api_key = settings.STRIPE_SECRET_KEY # settings.pyから秘密鍵を読み込む

    user = request.user
    user_id = user.id
    user_name = user.username
    product_id = Cart.objects.filter(user_id=user_id).values_list('product_id', flat=True) # ユーザーIDがログインしているユーザのIDになっている"products"を取り出す 追加(2021/09/09)
    products = Wine.objects.filter(id__in=product_id).values('id', 'name', 'price')
    price_total = Wine.objects.filter(id__in=product_id).aggregate(Sum('price'))['price__sum']
    price_total = round(price_total)

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'], # カード決済
            line_items=[ # 決済内容を記述
                {
                    'price_data': {
                        'currency': 'jpy', # 通貨（円）
                        'unit_amount': 2000, # 金額
                        'product_data': { # 商品説明・画像
                            'name': 'sample house',
                            'images': ['http://gahag.net/img/201606/12s/gahag-0095672681-1.jpg'],
                            },
                    },
                    'quantity': 1, # 個数
                },
            ],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('WineOpener:success')), # 成功すれば"success"へ
            cancel_url=request.build_absolute_uri(reverse('WineOpener:cancel')), # 中止すれば"cancel"へ
        )

        print(checkout_session.id)
        return JsonResponse({'id': checkout_session.id})
    except Exception as e:
        return JsonResponse({'error':str(e)})