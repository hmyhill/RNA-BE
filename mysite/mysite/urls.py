#Importing modules needed for the urls
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from article import views as article_views

app_name = "main"   

#Setting paths for the urls
urlpatterns = [
    path('api/admin/', admin.site.urls, name='admin_Page'),
    path('api/articles/', include('article.urls')),
    path("api/accounts/", include("django.contrib.auth.urls")),
    path("api/accounts/change-user-permissions/", accounts_views.change_user_permissions, name="change_user_permissions"),
    path("api/login/", accounts_views.signup, name='signup'),
    path("api/delete-user/", accounts_views.del_user, name='delete-user'),
    path('api/return_news_articles/', article_views.return_news_articles, name='return_news_articles'),
    path('api/settings/password/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('api/settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path("api", TemplateView.as_view(template_name="home.html"), name="home"),
]
