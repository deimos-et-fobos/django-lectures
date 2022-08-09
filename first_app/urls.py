"""first_proyect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from first_app import views

app_name = 'first_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('other/', views.other, name='other'),
    path('special/', views.special, name='special'),
    path('relative/', views.relative, name='relative'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('user_login/', views.user_login, name='user_login'),
    path('formpage', views.form_name_view, name='form_name'),
]
