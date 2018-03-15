"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from sign import views

# 路由文件
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index),
    path('accounts/login/', views.index),
    path('login_action/', views.login_action),
    path('event_manage/', views.event_manage),
    path('search_name/', views.search_name),
    path('search_phone/', views.search_phone),
    path('guest_manage/', views.guest_manage),
    path('sign_index/<int:eid>/', views.sign_index),
    path('sign_index2/<int:eid>/', views.sign_index2),
    path('sign_index_action/<int:eid>/', views.sign_index_action),
    path('logout/', views.logout),
    # path('api/', include('sign.urls')),
]
