from django.views.generic import ListView, DetailView
from .models import Product, Category, Tag, Country
from django.shortcuts import render
from pubs.models import Pub


class HomeView(ListView):
    model = Product
    template_name = 'products/home.html'
    context_object_name = 'products'


class IndexView(ListView):
    template_name = 'products/home.html'
    context_object_name = 'products'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'more_context': Pub.objects.order_by('-publish')[:4],
            'beer_context': Product.objects.order_by('-publish')[:4],
        })
        return context

    def get_queryset(self):
        return Product.objects.order_by('name')


def about(request):
    return render(request, 'products/about.html', {'title': 'About'})


def search(request):
    try:
        s = request.GET.get('s')
    except:
        s = None
    if s:
        products = Product.objects.filter(name__icontains=s)
        context = {'query': s, 'products': products}
        template = 'products/search.html'
    else:
        template = 'products/products.html'
        context = {}
    return render(request, template, context)


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 6
    

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


class CategoryListView(ListView):
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'products/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['category']
        products = Product.objects.filter(category=category)
        context['products'] = products
        return context


class TagListView(ListView):
    model = Tag
    template_name = 'products/tag_list.html'
    context_object_name = 'tags'


class TagDetailView(DetailView):
    model = Tag
    template_name = 'products/tag_detail.html'
    context_object_name = 'tag'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = context['tag']
        products = Product.objects.filter(tag=tag)
        context['products'] = products
        return context


class CountryListView(ListView):
    model = Country
    template_name = 'products/country_list.html'
    context_object_name = 'countries'


class CountryDetailView(DetailView):
    model = Country
    template_name = 'products/country_detail.html'
    context_object_name = 'country'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        country = context['country']
        products = Product.objects.filter(country=country)
        context['products'] = products
        return context

