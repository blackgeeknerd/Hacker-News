import requests
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from rest_framework import viewsets
from .serializers import NewsDbSerializer
from .models import NewsDB
from .forms import CreateNewsForm
from news_api import serializers




def home(request):  
    """
    Display all News from the Database, 
    and also paginates each page to be 5 items per page
    
    p = Paginator instance
    """
    
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    news_search = NewsDB.objects.filter(
        Q(by__icontains=q) |
        Q(title__icontains=q) |
        Q(score__icontains=q) |
        Q(type__icontains=q) |
        Q(username__icontains=q)
    ) 
      
    p = Paginator(news_search, 5)
    page_num = request.GET.get('page', 1)
    
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
        
        
    context = {'news_search': news_search}
    return render(request, 'news_api/home.html', context)

    


def get_news(request):
    """
    Display all News from the Database, 
    and also paginates each page to be 5 items per page
    
    p = Paginator instance
    """
    
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    news_search = NewsDB.objects.filter(
        Q(by__icontains=q) |
        Q(title__icontains=q) |
        Q(score__icontains=q) |
        Q(type__icontains=q) |
        Q(username__icontains=q)
        
    ) 
    
    #paginator instance with 5 news per page
    p = Paginator(news_search, 5)
    #return to first page if no query is passed to page
    page_num = request.GET.get('page', 1)
    
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
        
    context = {'news': page, 'news_search': news_search}
    return render(request, 'news_api/news.html', context)

        
           
def createNewsForm(request):
    form = CreateNewsForm()
    
    if request.method =='POST':
        form = CreateNewsForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('get-news')
    context= {'form': form}
    return render(request, 'news_api/add_edit_news.html', context)



def editNews(request, pk):
    news = NewsDB.objects.get(id=pk)
    form = CreateNewsForm(instance=news)
    
    if request.method == 'POST':
        form = CreateNewsForm(request.POST, instance=news)
        if form.is_valid:
            form.save()
            return redirect('get-news')
    context = {'form': form}
    return render(request, 'news_api/add_edit_news.html', context)


def deleteNews(request, pk):
    news = NewsDB.objects.get(id=pk)
    
    if request.method == 'POST':
        news.delete()
        return redirect('get-news')
    return render(request, 'news_api/delete.html', {'obj':news})


class NewsDBViewSet(viewsets.ModelViewSet):
    queryset = NewsDB.objects.all()
    serializer_class = NewsDbSerializer
    