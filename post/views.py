from ipaddress import ip_address
from itertools import count, product
from multiprocessing import context
from re import I, template
from django.db import models
from django.http.response import Http404, JsonResponse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Post, Like, PostDetail
from .forms import PostForm
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from banners.models import *
from django.contrib.auth.models import User
from django.db.models import  F
from django.views.generic.base import TemplateView
from accounts.models import *






def is_valid_queryparam(param):
    return param != '' and param is not None
    




def last_posts(request):
    last_posts = Post.objects.all().order_by('-posting_date')
    

    contex = {
        'post': last_posts
    }
    return render(request, 'last_posts.html', contex)


def premium(request):
    premium = Post.objects.filter(preminium=True)
    
    contex = {
        'premium': premium,
    }

    return render(request, 'premium.html', contex)



def insta_posts(request):
    post = Post.objects.filter(linktype='Instagram')

    query = request.GET.get('query')

    cat = request.GET.get('category')
    categories = Category.objects.all()

    if is_valid_queryparam(cat):
        post = post.filter(category__title__icontains=cat)
        
        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)


    if is_valid_queryparam(query):
        post = post.filter(title__icontains=query)

        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)

    return render(request, 'insta_posts.html', {'post': post, 'categories': categories})    



def wp_posts(request):
    post = Post.objects.filter(linktype='Whatsapp')

    query = request.GET.get('query')

    cat = request.GET.get('category')
    categories = Category.objects.all()

    if is_valid_queryparam(cat):
        post = post.filter(category__title__icontains=cat)
        
        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)


    if is_valid_queryparam(query):
        post = post.filter(title__icontains=query)

        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)

    return render(request, 'wp_posts.html', {'post': post, 'categories': categories})


def telegram_posts(request):
    post = Post.objects.filter(linktype='Telegram')

    query = request.GET.get('query')

    cat = request.GET.get('category')
    categories = Category.objects.all()

    if is_valid_queryparam(cat):
        post = post.filter(category__title__icontains=cat)
        
        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)


    if is_valid_queryparam(query):
        post = post.filter(title__icontains=query)

        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)

    return render(request, 'telegram_posts.html', {'post': post, 'categories': categories})





def youtube_posts(request):
    post = Post.objects.filter(linktype='Youtube')

    query = request.GET.get('query')

    cat = request.GET.get('category')
    categories = Category.objects.all()

    if is_valid_queryparam(cat):
        post = post.filter(category__title__icontains=cat)
        
        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)


    if is_valid_queryparam(query):
        post = post.filter(title__icontains=query)

        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)

    return render(request, 'youtube_posts.html', {'post': post, 'categories': categories})


def tiktok_posts(request):
    post = Post.objects.filter(linktype='TikTok')

    query = request.GET.get('query')

    cat = request.GET.get('category')
    categories = Category.objects.all()

    if is_valid_queryparam(cat):
        post = post.filter(category__title__icontains=cat)
        
        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)


    if is_valid_queryparam(query):
        post = post.filter(title__icontains=query)

        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)

    return render(request, 'tiktok_posts.html', {'post': post, 'categories': categories}) 


def facebook_posts(request):
    post = Post.objects.filter(linktype='Facebook')

    query = request.GET.get('query')

    cat = request.GET.get('category')
    categories = Category.objects.all()

    if is_valid_queryparam(cat):
        post = post.filter(category__title__icontains=cat)
        
        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)


    if is_valid_queryparam(query):
        post = post.filter(title__icontains=query)

        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)

    return render(request, 'facebook_posts.html', {'post': post, 'categories': categories}) 


def category(request):
    cat = Category.objects.all()

    contex = {
        'categories' : cat
    }

    return render(request, 'query.html', contex)



from django.http import HttpResponseRedirect

@login_required(login_url='/account/register/')
def post_create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            postum = form.save(commit=False)
            postum.user = request.user
            postum.save()
            
            post = Post.objects.all()
            categories = Category.objects.all()
            last_posts = Post.objects.all().order_by('-posting_date')[:30]
            premium = Post.objects.filter(preminium=True).order_by('?')[:6]
            users = User.objects.all()
            reklam = MainBanner.objects.all()
            cat = request.GET.get('category')
            banners = Banner.objects.all()
            profile = None
            
            if request.user.is_authenticated:
                profile = User.objects.get(username=request.user)


            query = request.GET.get('query')
            tg = request.GET.get('telegram')
            wp = request.GET.get('whatsapp')
            fb = request.GET.get('facebook')
            ins = request.GET.get('instagram')
            you = request.GET.get('youtube')
            tik = request.GET.get('tiktok')
            # nov = request.GET.get('social')

    

            like_say = Like.objects.all()
    


            if is_valid_queryparam(cat):
                post = post.filter(category__title__icontains=cat)
        
                contex = {
                    'post': post,
                }
                return render(request, 'query.html', contex)


            if is_valid_queryparam(query):
                post = Post.objects.filter(title__icontains=query)

                
                
                contex = {
                    'post': post,
                }

                return render(request, 'query.html', contex)
        
            value= True
            
            contex = {
                    'categories': categories,
                    'post': last_posts,
                    'user': users,
                    'reklam': reklam,
                    'banner': banners,
                    'premium': premium,
                    'profile': profile,
                    'like_say': like_say,
                    'value': value,
                }




    

            return render(request, 'index.html', contex)
            # return redirect('home')

    contex = {
        'form': form,
    }

    return render(request, 'insert-book.html', contex)
    
from django.urls.base import reverse_lazy



def home_view(request):

    post = Post.objects.all()
    categories = Category.objects.all()
    last_posts = Post.objects.all().order_by('-posting_date')
    premium = Post.objects.filter(preminium=True).order_by('?')

    users = User.objects.all()
    reklam = MainBanner.objects.all()
    cat = request.GET.get('category')
    banners = Banner.objects.all()
    profile = None
    
    if request.user.is_authenticated:
        profile = User.objects.get(username=request.user)


    query = request.GET.get('query')
    tg = request.GET.get('telegram')
    wp = request.GET.get('whatsapp')
    fb = request.GET.get('facebook')
    ins = request.GET.get('instagram')
    you = request.GET.get('youtube')
    tik = request.GET.get('tiktok')
    # nov = request.GET.get('social')

    

    like_say = Like.objects.all()
    


    if is_valid_queryparam(cat):
        post = post.filter(category__title__icontains=cat)
        
        contex = {
            'post': post,
        }
        return render(request, 'query.html', contex)


    if is_valid_queryparam(query):
        post = Post.objects.filter(title__icontains=query)

        
        
        contex = {
            'post': post,
        }

        return render(request, 'query.html', contex)
  
    
    
    contex = {
        'categories': categories,
        'post': last_posts,
        'user': users,
        'reklam': reklam,
        'banner': banners,
        'premium': premium,
        'profile': profile,
        'like_say': like_say,
        
    }




    

    return render(request, 'index.html', contex)







def post_update(request, id):
    post = get_object_or_404(Post, id=id)

    if not request.user == post.user:
        raise Http404
    
    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('home')

    contex = {
        'form': form,
    }

    return render(request, 'insert-book.html', contex)


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if not request.user == post.user:
         raise Http404
    post.delete()

    return redirect('home')



from accounts.models import Ip_adress, User_detail



def post_referance(request, id, username):

    userim = User.objects.get(username=username).id

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        userip = x_forwarded_for.split(',')[0]
    else:
        userip = request.META.get('REMOTE_ADDR')

    useripstr = userip


    user_id = User_detail.objects.get(user=userim).id

    ipadesler= Ip_adress.objects.filter(ip=userim)

    ip_list = list()

    # ipnin alinmasi, userin ipadress modeline yeni entry yaratmaq ve ipni ona menimsetmek, 


    for v in ipadesler:
        ip_list.append(v.ipadress) 

    if useripstr not in ip_list:
        new_ip = Ip_adress()

        new_ip.ip_id = user_id

        new_ip.ipadress = useripstr

        new_ip.save()


        coins = User_detail.objects.filter(user=user_id).update(coins=F('coins') + 1)
    
    else:
        pass
    
    
    return redirect('post-detail', id)

def post_referance(request, id, username):
    
    userim = User.objects.get(username=username).id

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        userip = x_forwarded_for.split(',')[0]
    else:
        userip = request.META.get('REMOTE_ADDR')

    useripstr = str(userip)



    user_ip = User.objects.get(username=username).last_name



    if useripstr != user_ip:

        coins = User_detail.objects.filter(user=userim).update(coins=F('coins') + 1)
    
    else:
        pass
    
    
    return redirect('post-detail', id)

# def post_detail(request, id):

#     post = Post.objects.get(id=id)
#     # staff = get_object_or_404(Post, id = id)
#     related_product = Post.objects.filter(category = post.category).exclude(id=id).filter(preminium=True).order_by('?')
#     # total_likes = staff.total_likes_received()
#     # like = staff.like()
#     blog_object=Post.objects.get(id=id)
#     blog_object.view_count=blog_object.view_count+1
#     blog_object.save()
#     context = {
#         "post" : post,
#         "related" : related_product
#     }
#     # context['total_likes'] = total_likes
#     # context['like_count'] = like
#     context['view_count'] = blog_object.view_count
#     return render(request, "details.html", context)
from accounts.models import Ip_adress, User_detail




def post_referance(request, id, username):
    post = Post.objects.get(id=id)

    userim = User.objects.get(username=username).id

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        userip = x_forwarded_for.split(',')[0]
    else:
        userip = request.META.get('REMOTE_ADDR')

    useripstr = str(userip)



    user_ip = User.objects.get(username=username).last_name

    

    if useripstr != user_ip:
        if post.preminium == True:
            coins = User_detail.objects.filter(user=userim).update(coins=F('coins') + 2)
        else:
            coins = User_detail.objects.filter(user=userim).update(coins=F('coins') + 1)
    else:
        pass
    
    
    return redirect('post-detail', id)

import datetime

def post_detail(request, id):

    post = Post.objects.get(id=id)
    staff = get_object_or_404(Post, id = id)
    related_product = Post.objects.filter(category = post.category).exclude(id=id).filter(preminium=True).order_by('?')
   
    blog_object=Post.objects.get(id=id)
    blog_object.view_count=blog_object.view_count+1
    blog_object.save()
    context = {
        "post" : post,
        "related" : related_product
    }
   
    context['view_count'] = blog_object.view_count
    # odenis yeri

    postid = request.GET.get('user_id')

    coins = request.GET.get('rangecoinsquery')

    days = request.GET.get('rangvaluequry')

    mainuserdetail = User_detail.objects.get(user=request.user)
    
   

    endalert = 0
   
    if postid:
        currentpost = Post.objects.get(id=int(postid))
        if currentpost.preminium == False:
            if int(coins) <= mainuserdetail.coins:
                Post.objects.filter(id=int(postid)).update(preminium=True)
                anal = User_detail.objects.filter(user=request.user).update(coins=F('coins') - int(coins))
                Post.objects.filter(id=int(postid)).update(preminium_days=int(days), preminium_date=datetime.datetime.now())
                
                
                endalert = 2
                
            else:
                
                endalert = 1
                
        
        else:
            
            endalert = 3
          

    postmoney = Post_money.objects.first()
    context['endalert'] = endalert
    context['postmoney'] = postmoney

    return render(request, "details.html", context)
def filter_product(request):
    category = request.GET.getlist('category[]')

    filterProducts = Post.objects.filter(
        product_category_list = category
    )

    return HttpResponse(filterProducts.query)




# def LikeView(request, id):
#     post = get_object_or_404(Post, id=request.POST.get('post_id'))

#     if not request.user.is_authenticated:
#             return HttpResponseRedirect(reverse('register')) 

#     if request.user.is_authenticated:
#         post.liked.add(request.user)

#         return HttpResponseRedirect(reverse('post-detail', args=[str(id)]))





def BannerLink(request):
    link = MainBanner.objects.all()
    context = {  
        'link': link,
    }
    return(render(request, 'index.html', context))


class Kesfet(TemplateView):
    template_name = "top50.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kesfet'] = Post.objects.order_by('-post_views')
        return context

from django.views import View

def top_50(request):
   
    view_count = Post.objects.order_by('-view_count')
    query = request.GET.get('query')
    # kesfet = Post.objects.order_by('-view_count')


    
    if is_valid_queryparam(query):
        post = Post.objects.filter(title__icontains=query)

        
        
        contex = {
            'post': post,
        }

        return render(request, 'query.html', contex)




    contex = {
        'kesfet': view_count,
    }
    return render(request, 'top50.html', contex)



class RelatedPost(TemplateView):
    template_name = 'details.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        context['related'] = Post.objects.all()
        return context



