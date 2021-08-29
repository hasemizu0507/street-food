from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import json
from streetfood.models import Food, Profile, Cart


def concept_top(request):
    user = request.user
    profile = user.profile
    user_id = user.id
    # owner_id=profile.idの商品を取り出し、テンプレートに渡す。
    myfoods = Food.objects.filter(owner_id=profile.id)
    # ユーザーIDがログイン中しているユーザのIDになっているproductsを取り出す。
    products = Cart.objects.filter(user_id=user_id)

    return render(request, 'streetfood/concept.html', {'profile':profile,'foods':myfoods, 'products': products}) #'assessments':myassessments
