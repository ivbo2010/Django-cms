from django.contrib import admin
from .models import Product, Category, Tag, Country


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description','category','country','tag','status','image_tag')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    #fields = ( 'name', 'description','category','tag','country','image','image_tag','status')
    readonly_fields = ('image_tag',)

    list_per_page = 10


admin.site.register(Product,ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','image_tag')
    list_display_links = ('id', 'name')
    search_fields = (['name'])
    #fields = ( 'name','image','image_tag')
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 10


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Country)