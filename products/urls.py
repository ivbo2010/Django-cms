from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import path, include
from .views import ProductListView, ProductDetailView, CategoryListView, CategoryDetailView, TagListView, TagDetailView, CountryListView, CountryDetailView, IndexView, search


urlpatterns = [
    #path('', views.home, name='home'),
	path('', IndexView.as_view(), name='home'),
    path('about/',views.about, name='about'),
    url(r'^s/', search, name='search'),
    path('list/', ProductListView.as_view(), name='products_list'),
    path('detail/<slug>', ProductDetailView.as_view(), name='product_detail'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('tag_list/', TagListView.as_view(), name='tag_list'),
    path('country_list/', CountryListView.as_view(), name='country_list'),
    path('category_detail/<slug>', CategoryDetailView.as_view(), name='category_detail'),
    path('tag_detail/<slug>', TagDetailView.as_view(), name='tag_detail'),
    path('country_detail/<int:pk>', CountryDetailView.as_view(), name='country_detail'),
]