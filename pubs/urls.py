from . import views
from django.conf.urls import url
from django.urls import path, include
from .views import PubListView, PubDetailView, PubCategoryListView, PubCategoryDetailView


urlpatterns = [

    path('list/', PubListView.as_view(), name='pub_list'),
    path('detail/<slug:slug>', PubDetailView.as_view(), name='pub_detail'),
    path('category_list/', PubCategoryListView.as_view(), name='pub_category_list'),
    path('category_detail/<slug>', PubCategoryDetailView.as_view(), name='pub_category_detail'),
]

