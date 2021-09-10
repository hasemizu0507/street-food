from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import json
from WineOpener.models import Profile, Wine, Cart # 変更(2021/09/08)
from django.contrib.auth.models import User

import random

def list_view(request):
    return render(request, 'WineOpener/live_list.html')

@login_required
def detail_view(request):
    wine_informations = Wine.objects.all().order_by('id')
    return render(request, 'WineOpener/live_detail.html', {'wine_informations': wine_informations})

def wine_view(request, livewine_id):
    wine_information = get_object_or_404(Wine, id=livewine_id)
    return render(request, 'WineOpener/live_wine.html', {'wine_information': wine_information})

def edit_cart(request, livewine_id): 
    wine_information = get_object_or_404(Wine, id=livewine_id)
    user_id = request.user.id #ログインしているユーザーのIDを取得

    previous_cart = Cart.objects.filter(user_id=user_id, product_id=livewine_id) # 修正必要
    if previous_cart.exists(): # 編集前のカートの中身にこの商品はある？
        previous_cart.delete() # あればその商品を削除
    else:
        product = Cart(user_id=user_id, product_id=livewine_id) # なければユーザーID，商品ID，商品名，価格をカートに追加
        product.save()
    return render(request, 'WineOpener/live_wine.html', {'wine_information': wine_information})