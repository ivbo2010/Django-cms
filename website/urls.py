from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from products.sitemaps import ProductSitemap

sitemaps = {
    'products': ProductSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    url(r'^', include('products.urls')),
    path('pub/', include('pubs.urls')),
    url(r'^pub/', include('pubs.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
