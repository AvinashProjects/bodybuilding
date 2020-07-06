"""bodybuilding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from gymapp.views import *

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('schedule/', schedule, name='schedule'),
    path('gallery/', gallery, name='gallery'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('blogdetail/', blogdetail, name='blogdetail'),
    path('form/', form, name='form'),
    path('elements/', elements, name='elements'),

    #-----Admin login and logout url---------
    path('login/', login_admin, name='login'),
    path('logout/', logout_admin, name='logout'),
    path('view_members/', view_members, name='view_members'),

    #----- Forget email urls-------------



    # path('password-reset/',auth_views.PasswordResetView.as_view(template_name='gymapp/password_reset.html'),name='password_reset'),
    #
    # path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='gymapp/password_reset_done.html'            ),name='password_reset_done'),
    #
    # path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='gymapp/password_reset_confirm.html'),name='password_reset_confirm'),
    #
    # path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='gymapp/password_reset_complete.html'),name='password_reset_complete'),
    path('', include('django.contrib.auth.urls'))
]
