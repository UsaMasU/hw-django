from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator
from .models import Book

template = 'books/books_list.html'


def books_view(request):
    return render(request, template, context = {
        'books': Book.objects.all()
    })


def books_pub_view(request):
    page_number = int
    url_str = request.get_full_path().split('/')
    pub_date = url_str[2]

    books = Book.objects.order_by("pub_date")

    for index, book in enumerate(books):
        if(str(book.pub_date) == str(pub_date)):
            page_number = index + 1

    paginator = Paginator(books , 1)
    page_object = paginator.get_page(page_number)
    books_show = paginator.page(page_object.number).object_list

    if (page_object.has_next()):
        next_page = str(books[page_object.next_page_number() - 1].pub_date)
    else:
        next_page = ''

    if (page_object.has_previous()):
        prev_page = str(books[page_object.previous_page_number() - 1].pub_date)
    else:
        prev_page = ''

    return render_to_response(template, context={
        'books':  books_show,
        'prev_page_url': prev_page,
        'next_page_url': next_page
    })
