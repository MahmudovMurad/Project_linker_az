# from django.conf.urls import url

from django.urls import include, path, re_path
# from django.conf.urls import url


from .views import *

urlpatterns = [
     path('add/', post_create, name='post_create'),
     path('(?P<id>\d+)/update/', post_update, name='update'),
     path('(?P<id>\d+)/delete/', post_delete, name='delete'),
     path('last-posts/', last_posts, name='last_posts'),
     path('premium-posts/', premium, name='premium'),
     path('kesfet/', top_50, name='top50'),
     path('telegram_posts/', telegram_posts, name='telegram_posts'),
     path('wp_posts/', wp_posts, name='wp_posts'),
     path('insta_posts/', insta_posts, name='insta_posts'),
     path('facebook_posts/', facebook_posts, name='facebook_posts'),
     path('youtube_posts/', youtube_posts, name='youtube_posts'),
     path('tiktok_posts/', tiktok_posts, name='tiktok_posts'),
     path('query_posts/', category, name='query_posts'),
     path('post-detail/<int:id>/', post_detail, name='post-detail'),
     # path('like/<int:id>/', LikeView, name='like_post'),
     path('<username>/<int:id>/', post_referance, name='post_referance'),

]
