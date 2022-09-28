"""Bhaas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from first import views, views1

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/', views.home, name = 'home'),
    path('', views.home, name = 'home'),
    path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login'),
    path('logout', views.logoutuser, name = 'logout'),
    path('list', views.list, name = 'list'),
    path('detail/<int:id>', views.detail, name = 'detail'),
    
    # path('detail/<int:id>', views.detail, name = 'detail'),
    
    path('proj1', views1.proj1, name = 'proj1'),
    path('detail_product/<int:id>', views1.detail_product, name = 'detail_product'),
    path('update/<int:id>', views1.update, name = 'update'),
    path('delete/<int:id>', views1.delete, name = 'delete'),
    
]
