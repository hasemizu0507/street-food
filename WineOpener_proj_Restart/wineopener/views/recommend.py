# [ REWRITE ]  ファイル追加
# /recommendと/recommend/resultのURIのときのViewを定義

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from wineopener.scripts.recommend_existing_user import Recommend_Existing
from wineopener.scripts.recommend_new_user import RecommendNew

from wineopener.models import wine

def form_view(request): # フォームを表示
    return render(request, 'wineopener/recommend_form.html') 

def result_view(request): # フォームの入力をAPIに伝達、リターン値を用いてテンプレートに表示
    var = request.GET
    use_profile = var.get('use_profile')
    if use_profile: #既存
        limit = int(var.get('limit',3))
        base = var.get('search_base','user')
        userid = int(request.user.id)
        results = Recommend_Existing().recommend(userid, limit, base)
        print("results", results)
    else: #新規
        age = int(var.get('age'))
        gender_str = var.get('gender') 
        if gender_str == 'male':
            gender = 0
        else:
            gender = 1
        household = int(var.get('household'))
        station = var.get('station')
        limit = int(var.get('limit',3))
        results = RecommendNew().recommend(age, station,limit)
        print("results", results)
    
    results = [(wine.objects.get(id=x), y) for (x,y) in results]
    return render(request, 'wineopener/recommend_result.html', {'results':results})
