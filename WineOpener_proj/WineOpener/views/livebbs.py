from rest_framework import status, views, response
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import json
from WineOpener.models import Profile, Wine, Cart, Topic # 変更(2021/09/10)
from WineOpener.serializer import TopicSerializer
from django.contrib.auth.models import User

import random

from django.template.loader import render_to_string

class BbsView(views.APIView):
    def get(self,request,*args,**kwargs):

        data        = Topic.objects.all()
        context     = {"data":data}
        return render(request,"WineOpener/live_detail.html",context)

    def post(self, request, *args, **kwargs):

        serializer      = TopicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data        = Topic.objects.all()
        context     = {"data":data}
        content_data_string     = render_to_string('WineOpener/comment.html', context ,request)
        json_data               = { "content" : content_data_string }

        return JsonResponse(json_data)

index   = BbsView.as_view()

class BbsDeleteView(views.APIView):

    def delete(self, request, pk, *args, **kwargs):

        topic           = get_object_or_404(Topic,pk=pk)
        topic.delete()

        data        = Topic.objects.all()
        context     = {"data":data}
        content_data_string     = render_to_string('WineOpener/comment.html', context ,request)
        json_data               = { "content" : content_data_string }

        return JsonResponse(json_data)

delete  = BbsDeleteView.as_view()