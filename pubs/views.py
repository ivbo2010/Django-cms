from django.views.generic import ListView, DetailView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Pub, PubCategory

from django.shortcuts import render
from django.urls import reverse_lazy


class PubListView(ListView):
    model = Pub
    template_name = 'pub/pub.html'
    context_object_name = 'pubs'


class PubDetailView(DetailView):
    model = Pub
    template_name = 'pub/pub_detail.html'
    context_object_name = 'pub'


class PubCategoryListView(ListView):
    model = PubCategory
    template_name = 'pub/category_list.html'
    context_object_name = 'pub_categories'


class PubCategoryDetailView(DetailView):
    model = PubCategory
    template_name = 'pub/category_detail.html'
    context_object_name = 'pub_category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pub_category = context['pub_category']
        pubs = Pub.objects.filter(pub_category=pub_category)
        context['pubs'] = pubs
        return context

