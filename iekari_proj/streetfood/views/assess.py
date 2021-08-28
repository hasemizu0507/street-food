# [ REWRITE ]  ファイル追加

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from iekari.scripts.predict_price import PricePredict

from iekari.models import RentRoom

def form_view(request): # フォームを表示
    return render(request, 'iekari/assessment_form.html') 

# +++++++++++++++++++++++++  追記1  +++++++++++++++++++++++++++
def isfloat(value):
  try:
    float(value) # とりあえずfloatにできるかどうか試してみて、
    return True # 正常にfloatに変換できればTrueを返して、
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
# +++++++++++++++++++++++++  追記1　ここまで  +++++++++++++++++++++++++++


def result_view(request): # フォームの入力をAPIに伝達、リターン値を用いてテンプレートに表示
    var = request.GET
    predict_price = PricePredict()
    # +++++++++++++++++++++++++  追記2  +++++++++++++++++++++++++++
    if "station" not in request.GET or not isfloat(var.get("station")):
        return createErrorResponse("stationパラメータが正しくセットされていません. 入力をやり直して下さい", "/iekari/assess")
    if "area" not in request.GET or not isfloat(var.get("area")):
        return createErrorResponse("areaパラメータが正しくセットされていません. 入力をやり直して下さい", "/iekari/assess")
    if "year" not in request.GET or not isfloat(var.get("year")):
        return createErrorResponse("yearパラメータが正しくセットされていません. 入力をやり直して下さい", "/iekari/assess")
    # +++++++++++++++++++++++++  追記2　ここまで  +++++++++++++++++++++++++++
    else:
        station = float(var.get("station"))
        area = float(var.get("area"))
        year = float(var.get("year"))
        predict_price.load_model("./iekari/scripts/price_model.sav")
        result = predict_price.predict(dist_to_nearest_station =station, area =area, year_pp =year)
        return render(request, 'iekari/assessment_result.html', {"station":station, "area":area, "year":year, 'result':int(result*area)}) # templateに学習結果を辞書型で送るイメージ…？
    