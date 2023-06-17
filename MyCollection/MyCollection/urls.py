"""
URL configuration for MyCollection project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import Authentication.views
import Listings.views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", Listings.views.home, name="home"),
    path(
        "",
        LoginView.as_view(
            template_name="Authentication/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    path("signup/", Authentication.views.signup_page, name="signup"),
    path(
        "change-password/",
        PasswordChangeView.as_view(
            template_name="Authentication/password_change_form.html"
        ),
        name="password_change",
    ),
    path(
        "change-password-done/",
        PasswordChangeDoneView.as_view(
            template_name="Authentication/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("books/", Listings.views.show_books, name="show-books"),
    path("add-book/", Listings.views.add_book, name="add-book"),
    path("books/delete/<int:book_id>/", Listings.views.delete_book, name="delete_book"),
    path("search_book/", Listings.views.search_book, name="search_book"),
    path("books/<int:book_id>/", Listings.views.book_detail, name="book_detail"),
    path("genres/", Listings.views.liste_genre, name="liste_genre"),
    path(
        "livres-by-genre/<int:genre_id>/",
        Listings.views.livres_by_genre,
        name="livres_by_genre",
    ),
    path("books/<int:book_id>/update/", Listings.views.update_book, name="update_book"),
]
