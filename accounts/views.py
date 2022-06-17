from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from  django.contrib.auth import logout
from django.contrib import messages
from accounts.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from accounts.models import User_detail
# from .forms import User_detail_form
from post.models import Post
from accounts.models import User_detail
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from . forms import*
from django.views.generic import TemplateView

from django.utils.http import urlsafe_base64_decode
def loginview(request):
    form = LoginForm(request.POST or None)
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))



    
    if form.is_valid():
        
        username= form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
                
        return redirect('home')
        



    contex = {
        'form': form,
    }

    return render(request, 'sign-in.html', contex)



def registerview(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    


    
    
    form = RegisterForm(request.POST or None)
    
    deatil = User_detail()

    
    next= ""
    if request.GET:
        next = request.GET['next']


    if form.is_valid():
        user= form.save(commit=False)
        password= form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user= authenticate(username=user.username, password=password)
        login(request, new_user)

        

        deatil.user = request.user
        deatil.coins = 0

        deatil.save()
        if next=='':
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('post_create'))
    
  

    contex = {
        'form': form,
    }

    return render(request, 'sign-up.html', contex)
    
def log_out(request):
    logout(request)
    return redirect('home')




def profil(request, username):
    user = get_object_or_404(User, username=username)


    user_id = user.id

    coins = User_detail.objects.get(user=user_id).coins

    if not request.user == user:
        raise Http404

    logged_in_user = request.user
    logged_in_user_posts = Post.objects.filter(user=user)

    contex={

        'post_list': logged_in_user_posts,
        'login': logged_in_user,
        'user_id': coins,
    }
    return render(request, 'personal-cabinet.html', contex)







# Password Reset 

