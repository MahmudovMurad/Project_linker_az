from django.contrib import admin
from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'user']
    list_filter = ['id', 'category', 'user']


admin.site.register(Category)
admin.site.register(Like)
admin.site.register(PostDetail)

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('category',)
#     list_filter = ('category',)