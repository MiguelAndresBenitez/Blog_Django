from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create-post/', views.create_post, name='create_post'),
    path('my_posts/', views.my_posts, name='my_posts'), 
    path('post/<int:post_id>/delete', views.delete_post, name='delete_post'),
    path('update_post/<int:post_id>', views.update_post, name='update_post')
]