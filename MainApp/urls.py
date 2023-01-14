from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog/<str:slug>/', views.blog_single, name='blog_single'),
    path('search', views.search, name='search'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
