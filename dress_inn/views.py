# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render
import json

from .utils import scrape_popular_items, auth_user
from users.forms import UserForm

@csrf_exempt
def scrape_diesel(request):
    # POSTメソッドだけでリクエストしてくる想定
    form = UserForm(request.POST)
    form.is_valid()  # エラーを出さない想定
    if not auth_user(form.cleaned_data['user_id'], form.cleaned_data['password']):
      return "正しいユーザーIDとパスワードを送ってください"

    url = "https://www.dressinn.com/%E3%83%95%E3%82%A1%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3/diesel/303/mm"
    json_obj = scrape_popular_items(url)

    return HttpResponse(json_obj, content_type='application/json')
