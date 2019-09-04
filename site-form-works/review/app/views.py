from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()
    print('products view')

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    print('product')
    template = 'app/product_detail.html'

    if request.method == 'POST':
        print('post')
        product = get_object_or_404(Product, id=pk)

        form = ReviewForm
        if request.method == 'POST':
            # логика для добавления отзыва
            pass

        context = {
            'form': form,
            'product': product
        }
        return render(request, template, context)
    else:
        form = ReviewForm
        product = {}
        context = {
            'form': form,
            'product': product
        }
    return render(request, template, context)


