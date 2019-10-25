"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path, include
from . import views
from .views import (
    PostListView,
    DetailListView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    PostCreateView)

urlpatterns = [
    path('', PostListView.as_view(), name='myblog-home'),
    path('post/int:<pk>/', DetailListView.as_view(), name='detail_view'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/int:<pk>/update', PostUpdateView.as_view(), name='update_view'),
    path('post/int:<pk>/delete', PostDeleteView.as_view(), name='delete_view'),
    path('post/new/', PostCreateView.as_view(), name='create_view'),
    path('about/', views.about, name='myblog-about')
]
