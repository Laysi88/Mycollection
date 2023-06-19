from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Book, Genre
from .forms import BookForm


@login_required
def home(request):
    return render(request, "Listings/home.html")


@login_required
def show_books(request):
    books = Book.objects.filter(user=request.user).order_by("name")
    paginator = Paginator(books, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    total_price = Book.calculate_total_price(request.user)
    return render(
        request,
        "Listings/show_books.html",
        {"page_obj": page_obj, "total_price": total_price},
    )


@login_required
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect("show-books")
    else:
        form = BookForm()

    context = {"form": form}
    return render(request, "Listings/add_book.html", context)


@login_required
def liste_genre(request):
    genres = Genre.objects.filter(book__user=request.user).distinct()
    return render(request, "Listings/liste_genre.html", {"genres": genres})


@login_required
def livres_by_genre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    livres = Book.objects.filter(genre=genre, user=request.user).order_by("name")
    paginator = Paginator(livres, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request, "Listings/livres_by_genre.html", {"genre": genre, "page_obj": page_obj}
    )


@login_required
def delete_book(request, book_id):
    user = request.user
    book = get_object_or_404(Book, id=book_id, user=user)
    book.delete()
    return redirect("show-books")


@login_required
def search_book(request):
    query = request.GET.get("query")
    books = (
        Book.objects.filter(user=request.user, name__icontains=query) if query else []
    )
    return render(
        request, "Listings/search_book.html", {"books": books, "query": query}
    )


@login_required
def book_detail(request, book_id):
    user = request.user
    book = get_object_or_404(Book, id=book_id, user=user)
    return render(request, "Listings/book_detail.html", {"book": book})


@login_required
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id, user=request.user)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("livres_by_genre", genre_id=book.genre.id)
    else:
        form = BookForm(instance=book)

    return render(request, "Listings/update_book.html", {"form": form, "book": book})
