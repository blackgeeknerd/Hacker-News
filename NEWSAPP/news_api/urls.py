from rest_framework import routers
from multiprocessing.managers import Namespace
from django.urls import path, include
from . import views

from .views import *




router = routers.DefaultRouter()
router.register(r'newsdb', NewsDBViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.get_news, name='get-news'),
    # path('show/', views.display_front, name='display-front'),
    path('create-news/', views.createNewsForm, name='create-news'),
    path('edit-news/<str:pk>', views.editNews, name='edit-news'),
    path('delete-news/<str:pk>', views.deleteNews, name='delete-news'),


    path('news-api/', include(router.urls))
    
    # path('newsapi/', include('rest_framework.urls', namespace='rest_framework'))
]
