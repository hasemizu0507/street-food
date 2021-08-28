# [ REWRITE ]  ファイル追加
# /recommendと/recommend/resultのURIのときのViewを定義

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from iekari.scripts.recommend_existing_user import Recommend_Existing
from iekari.scripts.recommend_new_user import RecommendNew

from iekari.models import RentRoom

def form_view(request): # フォームを表示
    return render(request, 'iekari/recommend_form.html') 

# +++++++++++++++++++++++++  追記  +++++++++++++++++++++++++++
def isint(value):
  try:
    int(value) # とりあえずintにできるかどうか試してみて、
    return True # 正常にstrに変換できればTrueを返して、
  except ValueError: # エラーが出たら、
    return False # Falseをかえす

def isstr(value):
  try:
    str(value) # とりあえずstrにできるかどうか試してみて、
    return True # 正常にstrに変換できればTrueを返して、
  except ValueError: # エラーが出たら、
    return False # Falseをかえす

def createErrorResponse(msg, to):
    #Ref : https://stackoverflow.com/questions/11869662/display-alert-message-and-redirect-after-click-on-accept/11869779
    return HttpResponse(
        """
        <html>
            <script> 
                alert('{}'); 
                window.location.href='{}'; 
            </script>
            <body><h1>{}</h1></body> 
        </html>
        """.format(msg, to, msg)
    )
# +++++++++++++++++++++++++  追記  +++++++++++++++++++++++++++


def result_view(request): # フォームの入力をAPIに伝達、リターン値を用いてテンプレートに表示
    var = request.GET
    use_profile = var.get('use_profile')
    if use_profile: # 既存
        if "limit" not in request.GET or not isint(var.get('limit',3)):
            return createErrorResponse("limitパラメータが正しくセットされていません. 入力をやり直して下さい", "/iekari/recommend")
        else:
            limit = int(var.get('limit',3))
            base = var.get('search_base','user')
            userid = int(request.user.get_username()[1:])
            results = Recommend_Existing().recommend(userid, limit, base)
            print("results", results)
    else: #新規
        if "age" not in request.GET or not isint(var.get("age")):
            return createErrorResponse("ageパラメータが正しくセットされていません. 入力をやり直して下さい", "/iekari/recommend")
        if "household" not in request.GET or not isint(var.get("household")):
            return createErrorResponse("householdパラメータが正しくセットされていません. 入力をやり直して下さい", "/iekari/recommend")
        if "station" not in request.GET or not isstr(var.get("station")):
            return createErrorResponse("stationパラメータが正しくセットされていません. 入力をやり直して下さい", "/iekari/recommend")
        if "limit" not in request.GET or not isint(var.get('limit', 3)):
            return createErrorResponse("limitパラメータが正しくセットされていません. 入力をやり直して下さい", "/iekari/recommend")
        else:
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
    
    results = [(RentRoom.objects.get(id=x), y) for (x,y) in results]
    return render(request, 'iekari/recommend_result.html', {'results':results})

'''
def result_view(request): # フォームの入力をAPIに伝達、リターン値を用いてテンプレートに表示
    var = request.GET
    use_profile = var.get('use_profile')
    if use_profile: #既存
        limit = int(var.get('limit',3))
        base = var.get('search_base','user')
        userid = int(request.user.get_username()[1:])
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
    
    results = [(RentRoom.objects.get(id=x), y) for (x,y) in results]
    return render(request, 'iekari/recommend_result.html', {'results':results})
'''