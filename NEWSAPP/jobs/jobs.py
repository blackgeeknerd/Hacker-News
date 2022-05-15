from django.conf import settings
from django.shortcuts import render, redirect
import json
import requests
from django.utils import timezone
from news_api.models import NewsDB
from datetime import datetime



def schedule_api():
    """
    Method that Calls the Hacker news api at 5min Scheduled interval
    
        - Extract values from the first Http request and fix into 'items' Url 
        - Call on the items API
        - Save informations from the item Http request into the database  
    """
    
    empt = []
    urlList = []
    
    url = 'https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty'
    urlreal = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'

    response = requests.get(url)
    data = response.json()[:100]
    for datas in range(len(data)-1):
        empt.append(data[datas])
    
    for fix in range(len(empt)):
        get_comp_url = urlreal.format(empt[fix])
        # req_json = urlList.append(requests.get(get_comp_url).json())
        req_json = requests.get(get_comp_url).json()
        set_time = datetime.fromtimestamp(req_json['time'])
        
        NewsDB.objects.create(
        by=req_json['by'],
        news_id=int(req_json['id']),
        score=int(req_json['score']),
        time=set_time,
        text=req_json.get('text', ""),
        url=req_json.get('url', ""),
        type=req_json.get('type', ""),
        title=req_json['title'],
   
    )
    print('hello !st 3 minutes..check database')
    