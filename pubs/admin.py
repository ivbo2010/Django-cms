from django.contrib import admin
from .models import Pub, PubCategory


class PubAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','description','pub_category','status','image_tag')
    list_display_links = ('id', 'name')
    search_fields = (['name'])
    prepopulated_fields = {'slug': ('name',)}
    #fields = ( 'name','description','pub_category','image','image_tag')
    readonly_fields = ('image_tag',)
    list_per_page = 10


admin.site.register(Pub, PubAdmin)


class PubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','image_tag')
    list_display_links = ('id', 'name')
    search_fields = (['name'])
    fields = ( 'name','slug','image','image_tag')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('image_tag',)

    list_per_page = 10


admin.site.register(PubCategory, PubCategoryAdmin)

