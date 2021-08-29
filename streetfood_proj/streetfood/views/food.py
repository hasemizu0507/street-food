from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages

from django.contrib.auth.decorators import login_required #追加(2021.08.29.14:01)

from streetfood.models import Profile, Food, Cart
from django.contrib.auth.models import User #User追加
from django.core.paginator import Paginator
from streetfood.models import Food

import random

def list_view(request):
    food_list = Food.objects.all().order_by('-id')
    paginator = Paginator(food_list, 20) # ページ当たり20個表示

    try:
        page = int(request.GET.get('page'))
    except:
        page = 1

    foods = paginator.get_page(page)
    return render(request, 'streetfood/food_list.html', {'foods': foods, 'page': page, 'last_page': paginator.num_pages})

def detail_view(request, food_id):
    food = get_object_or_404(Food, id=food_id)

    try:
        page = int(request.GET.get('from_page'))
    except:
        page = 1
    return render(request, 'streetfood/food_detail.html', {'food': food, 'page': page })

def edit_cart(request, food_id):
    #表示しているページの物件を取得
    food = get_object_or_404(Food, id=food_id)
    #遷移前の一覧ページを取得
    try:
        page = int(request.GET.get('from_page'))
    except:
        page = 1
    #ログインしているユーザのIDを取得
    user_id = request.user.id
    #編集前のカートの中身にこの商品はある？
    previous_cart = Cart.objects.filter(user_id=user_id, product_id=food_id)
    if previous_cart.exists():
        #あればその商品を削除
        previous_cart.delete()
    else:
        #無ければユーザID・商品IDの組をカートに追加
        #productはCartクラスのインスタンス
        product = Cart(user_id=user_id, product_id=food_id)
        product.save()
    return render(request, 'streetfood/food_detail.html', {'food': food, 'page': page })