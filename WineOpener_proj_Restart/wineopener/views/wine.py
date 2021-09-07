from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages

from django.contrib.auth.decorators import login_required 

from wineopener.models import Profile, wine, Cart #Cart追加
from django.contrib.auth.models import User #User追加
from django.core.paginator import Paginator
from wineopener.models import wine

import random

def list_view(request):
    wine_list = wine.objects.all().order_by('-id')
    paginator = Paginator(wine_list, 20) # ページ当たり20個表示

    try:
        page = int(request.GET.get('page'))
    except:
        page = 1

    wines = paginator.get_page(page)
    return render(request, 'wineopener/wine_list.html', {'wines': wines, 'page': page, 'last_page': paginator.num_pages})



@login_required
def detail_view(request, wine_id):
    wine = get_object_or_404(wine, id=wine_id)

    try:
        page = int(request.GET.get('from_page'))
    except:
        page = 1
    return render(request, 'wineopener/wine_detail.html', {'wine': wine, 'page': page })

def edit_cart(request, wine_id):
    #表示しているページの物件を取得
    wine = get_object_or_404(wine, id=wine_id)
    #遷移前の一覧ページを取得
    try:
        page = int(request.GET.get('from_page'))
    except:
        page = 1
    #ログインしているユーザのIDを取得
    user_id = request.user.id
    #編集前のカートの中身にこの商品はある？
    previous_cart = Cart.objects.filter(user_id=user_id, product_id=wine_id)
    if previous_cart.exists():
        #あればその商品を削除
        previous_cart.delete()
    else:
        #無ければユーザID・商品IDの組をカートに追加
        #productはCartクラスのインスタンス
        product = Cart(user_id=user_id, product_id=wine_id)
        product.save()
    return render(request, 'wineopener/wine_detail.html', {'wine': wine, 'page': page })