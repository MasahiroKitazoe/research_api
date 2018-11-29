# coding: utf-8

from django.shortcuts import render
import json

from .utils import scrape_popular_items, auth_user

def scrape_diesel(request):
    user_id = request.GET['user_id']
    password = request.GET['password']
    if not auth_user():
      return "正しいユーザーIDとパスワードを送ってください"

    url = "https://www.dressinn.com/%E3%83%95%E3%82%A1%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3/diesel/303/mm"
    json_obj = scrape_popular_items(url)

    return json_obj
