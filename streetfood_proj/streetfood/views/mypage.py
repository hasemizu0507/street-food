from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import json
from streetfood.models import Food


@login_required
def mypage_top(request):
    user = request.user
    profile = user.profile
    # owner_id=profile.idの商品を取り出し、テンプレートに渡す。
    myfoods = Food.objects.filter(owner_id=profile.id)

    return render(request, 'streetfood/mypage.html', {'profile':profile,'foods':myfoods}) #'assessments':myassessments
