#Importing modules for the url paths
from . import views
from django.urls import path
from accounts import views as accounts_views

#Setting the URL paths for the articles
urlpatterns = [
    path('articles/', views.PostList.as_view(), name='articles'),
    path('search-articles/', views.BlogSearchView.as_view(), name='search-articles'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('signup/', accounts_views.signup, name='signup'),

    ]