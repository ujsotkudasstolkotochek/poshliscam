from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name = 'home'),
    path('create-bin/', views.create_bin, name = 'create_bin'),
    path('bin_page/<str:pk>/', views.bin_page, name = 'bin'),
    path('update-bin/<str:pk>/', views.update_bin, name = 'update_bin'),
    path('delete-bin/<str:pk>/', views.delete_bin, name = 'delete_bin'),
    path('login/', views.login_page, name = 'login'),
    path('logout/', views.logout_page, name = 'logout'),
    path('register/', views.register_page, name = 'register'),
    path('delete-comment/<str:pk>/', views.delete_comment, name = 'delete_comment'),
    path('user-profile/<str:pk>/', views.user_profile, name = 'user_profile'),
    path('like/<str:pk>/',views.like_bin, name = 'like_bin'),
    path('like_from_bin/<str:pk>/',views.like_from_bin, name = 'like_from_bin'),
    path('like_from_profile/<str:pk>/', views.like_from_profile, name='like_from_profile'),
    path('update_user/',views.update_user, name = 'update_user')
]