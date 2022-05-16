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
    path('create-news/', views.createNewsForm, name='create-news'),
    path('edit-news/<str:pk>', views.editNews, name='edit-news'),
    path('delete-news/<str:pk>', views.deleteNews, name='delete-news'),

    #url for API(both POST and GET,)..
    #when calling , specify the method(GET or POST)
    path('news-api/', include(router.urls))
    
]
