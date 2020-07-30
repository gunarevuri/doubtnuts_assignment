"""doubtnuts URL Configuration

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
from django.urls import path
from VidSolutions.views import index, get_class_videos,users_list, get_all_videos,get_all_classes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('users/', users_list, name='users_list'),
    path('videos/', get_all_videos, name='get_all_videos'),
    path('classes/', get_all_classes, name='get_all_classes'),
    path('downloads/video_solution/class/<int:id>/', get_class_videos, name='get_class_videos'),
]
