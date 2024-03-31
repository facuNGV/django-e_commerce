from django.contrib import admin


from e_commerce.models import *


@admin.register(Comic)
class ComicsAdmin(admin.ModelAdmin):
    list_display = ('marvel_id', 'title', 'stock_qty', 'price')

    list_filter= ('marvel_id','title')

    search_fields = ['title']

    fieldsets = (
        (None, {
            'fields': ('marvel_id', 'title', 'stock_qty')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('description','price', 'picture'),
        }),
    )


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('user', 'comic', 'favorite', 'cart')
    list_display_links = ('user', 'comic')
    list_filter= ('favorite','cart')