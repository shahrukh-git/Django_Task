from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, HttpResponseRedirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Product
from myapp.models import Post, User
from django.contrib.auth.models import Group

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'myproduct/home.html',{'posts':posts})
    # return render(request, 'myproduct/home.html')



def user_dashboard(request):
    if request.user.is_authenticated:    
        posts = Post.objects.all()
        # user = request.user
        # full_name = user.get_full_name()
        # gps = user.groups.all()
        return render(request, 'myproduct/dashboard.html', {'posts':posts})
    else:
        return HttpResponseRedirect('/')
    return render(request, 'myproduct/dashboard.html')



def user_login(request):
    if request.method == "POST":
        username1 = request.POST['username']
        password1 = request.POST['password']
        user = authenticate(username='username1', password='password1')
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully !')
            return HttpResponseRedirect('/dashboard/')
        else:
            return HttpResponseRedirect('/login/')
    else:
        return render(request, 'myproduct/login.html')



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')



# def add_post(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = PostForm(request.POST)
#             if form.is_valid():
#                 title = form.cleaned_data['title']
#                 description = form.cleaned_data['description']
#                 pst = Post(title=title, description=description)
#                 pst.save()
#                 form = PostForm()
#         else:
#             form = PostForm()
#         return render(request, 'blog/addpost.html', {'form':form})
#     else:
#         return HttpResponseRedirect('/login/')  



# def update_post(request, id):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             pi = Post.objects.get(pk=id)
#             form = PostForm(request.POST, instance=pi)
#             if form.is_valid():
#                 form.save()
#         else:
#             pi = Post.objects.get(pk=id)
#             form = PostForm(instance=pi)
#         return render(request, 'blog/updatepost.html', {'form':form})
#     else:
#         return HttpResponseRedirect('/login/')  


# def delete_post(request, id):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             pi = Post.objects.get(pk=id)
#             pi.delete()
#             return HttpResponseRedirect('/dashboard/')
#     else:
#         return HttpResponseRedirect('/login/')  
