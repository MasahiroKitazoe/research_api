# coding: utf-8

from django.shortcuts import render
import json

from scrape import scrape_popular_items

def scrape_diesel()
    url = "https://www.dressinn.com/%E3%83%95%E3%82%A1%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3/diesel/303/mm"
    json_obj = scrape_popular_items(url)

    return json_obj
