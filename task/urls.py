"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from myproduct import views as myviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myviews.home),
    path('dashboard/', myviews.user_dashboard, name='dashboard'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', myviews.user_login, name='login'),
    path('logout/', myviews.user_logout, name='logout'),
    # path('addpost/', views.add_post, name='addpost'),
    # path('updatepost/<int:id>/', views.update_post, name='updatepost'),
    # path('deletepost/<int:id>/', views.delete_post, name='deletepost')
]