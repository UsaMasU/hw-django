from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    if not('reviewed_products' in request.session):
        request.session['reviewed_products'] = []
    #del request.session['reviewed_products']

    context = {
        'product_list': products
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review(text=form.cleaned_data['text'], product=product)
            review.save()

            session_store = request.session['reviewed_products']
            session_store.append(product.name)
            request.session['reviewed_products'] = session_store

            return redirect(reverse('product_detail', args=[product.pk]))
    else:
        form = ReviewForm
        reviews = Review.objects.all().filter(product=product)

        is_review_exist = True if request.session['reviewed_products'].count(product.name) >= 1 else False

        context = {
            'form': form,
            'product': product,
            'reviews': reviews,
            'is_review_exist': is_review_exist
        }
        return render(request, template, context)



