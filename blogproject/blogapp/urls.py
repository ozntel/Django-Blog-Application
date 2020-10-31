from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.MainView, name='MainView'),
    path('post/<int:pk>', views.PostDetailView, name='PostDetailView'),
    path('post/create', views.PostCreateView.as_view(), name='PostCreateView'),
    path('post/<int:pk>/edit', views.PostEditView.as_view(), name='PostEditView'),
    path('post/<int:pk>/approve', views.ApprovePost, name='ApprovePost'),
    path('myposts/', views.MyArticlesView, name='MyArticlesView'),
    path('likepost/<int:pk>', views.LikePost, name='LikePost'),
    path('noaccess/', views.NoAccess, name='NoAccess'),
    path('login/', views.LoginView, name='LoginView'),
    path('logout/', views.LogoutView, name='LogoutView'),
] 