'''
from django.shortcuts import render, redirect, get_object_or_404

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import json
from iekari.models import RentRoom

@login_required
def mypage_top(request):
    user = request.user
    profile = user.profile
    # owner_id=profile.idの物件を取り出し、テンプレートに渡す。
    myrooms = RentRoom.objects.filter(owner_id=profile.id)
    print(user, profile, myrooms)
    return render(request, 'iekari/mypage.html', {'profile':profile,'rooms':myrooms}) #'assessments':myassessments
'''

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import json
from iekari.models import RentRoom, Profile, Cart

@login_required
def mypage_top(request):
    user = request.user
    profile = user.profile
    user_id = user.id
    myrooms = RentRoom.objects.filter(owner_id=profile.id)
    # ユーザーIDがログイン中しているユーザのIDになっているproductsを取り出す。
    products = Cart.objects.filter(user_id=user_id)
    return render(request, 'iekari/mypage.html', {'profile':profile,'rooms':myrooms, 'products':products}) #'assessments':myassessments