from email.mime import image
from os import link
from tokenize import Comment
from unicodedata import category
from django.db import models
from django.template import context
from django_resized import ResizedImageField
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.db import models

from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation


# from django.utils.encoding import python_2_unicode_compatible

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title

# @python_2_unicode_compatible
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True, related_name='posts', verbose_name='İstifadəçi')
    
    link = models.CharField(verbose_name='Link', max_length=1000)
    
    title = models.CharField(max_length=255, verbose_name='Qrupun adı')

    description = models.TextField(verbose_name='Qrup haqqında', max_length=2000, blank=True, null=True)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategoriya')
    
    TYPE = (
        ('Whatsapp', 'Whatsapp'),
        ('Telegram', 'Telegram'),
        ('Facebook', 'Facebook'),
        ('Youtube', 'Youtube'),
        ('TikTok', 'TikTok'),
        ('Instagram', 'Instagram'),
    )
    
    linktype = models.CharField(choices=TYPE ,max_length=100, verbose_name='Platforma', blank=True, null=True)

    image = ResizedImageField(size=[1280, 720], quality=80, verbose_name="Sekil", force_format='JPEG',blank = True, null = True)

    like_count = models.IntegerField(verbose_name="Like sayı", default=0, blank=True, null=True)

    slug = models.SlugField(max_length=100,blank=True ,null=True,unique=True)

    liked = models.ManyToManyField(User,blank=True, related_name='post_like')

    view_count = models.IntegerField(verbose_name="Baxış sayı", default=0)

    preminium = models.BooleanField(verbose_name="Preminium", default=False)

    posting_date = models.DateTimeField(auto_now_add=True, verbose_name="Yüklənmə vaxtı")

    updatedate = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    wp_link = models.CharField(verbose_name="linker wp ",max_length=1000, blank=True, null=True)

    # hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
    #  related_query_name='hit_count_generic_relation')
    
    

    def __str__(self) -> str:
        return self.title


    def get_absolute_url(self):
        return reverse_lazy('post:post_detail', kwargs={
            'id': self.id
        })


    def total_likes_received(self):
        return self.liked.count()


    def like(self, *args, **kwargs):
        self.like_count = self.liked.count()
        return super().save(*args, **kwargs)
   




class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class PostDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Post_detail_images/')
    like = models.IntegerField(verbose_name="like", default=0, blank=True, null=True)
    text = models.TextField(verbose_name="Mətn", blank=True, null=True)   






