"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from accounts import views as account_views
from django.conf import settings
from django.conf.urls.static import static

from books import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BookListView.as_view(), name='home'),

    path('signup/', account_views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'), name='login'),

    path('settings/my_account', account_views.UserUpdateView.as_view(), name='my_account'),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='email_password_reset.html',
        subject_template_name='subject_password_reset.txt'
    ), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('reset_password/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),
    path('settings/password_change/', auth_views.PasswordChangeView.as_view(
        template_name='password_change.html'
    ), name='password_change'),
    path('settings/password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'
    ), name='password_change_done'),

    path('my_account/my_books/', views.MyBookListView.as_view(), name='my_books'),
    path('my_account/my_books/upload_book/', views.upload_book, name='upload_book'),
    path('my_account/my_books/<slug:slug>/book_homepage/', views.ChapterListView.as_view(), name='book_homepage'),
    path('my_account/my_books/<slug:slug>/book_homepage/update_book/',
         views.BookUpdateView.as_view(),
         name='update_book'
         ),
    path('my_account/my_books/<slug:slug>/book_homepage/upload_chapter/', views.upload_chapter, name='upload_chapter'),
    path('my_account/my_books/<slug:slug>/book_homepage/<slug:slug_chapter>/',
         views.chapter_content,
         name='chapter_content'
         ),
    path('my_account/my_books/<slug:slug>/book_homepage/<slug:slug_chapter>/edit_chapter/',
         views.ChapterUpdateView.as_view(),
         name='edit_chapter'
         ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
