import urllib.parse
from pprint import pprint

from django.core.paginator import Paginator
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.urls import reverse

from .models import Product, Review, Phone  # app_eshop
from .forms import ReviewForm


def pagination(request, model_obj, objects_to_page):
    page_number = request.GET.get('page')
    paginator = Paginator(model_obj, objects_to_page)
    page_object = paginator.get_page(page_number)
    objects_show = paginator.page(page_object.number).object_list

    if page_object.has_next():
        next_page = '?' + urllib.parse.urlencode({'page': page_object.next_page_number()})
    else:
        next_page = ''
    if page_object.has_previous():
        prev_page = '?' + urllib.parse.urlencode({'page': page_object.previous_page_number()})
    else:
        prev_page = ''

    context = {
        'objects': objects_show,
        'current_page': page_object.number,
        'prev_page_url': prev_page,
        'next_page_url': next_page,
        'num_pages': list(range(1, paginator.num_pages + 1))
    }
    return context


def index(request):
    return redirect(reverse(main))


def main(request):
    template_name = 'app_eshop/index.html'
    phones = Product.objects.filter(section__startswith='smartphones').order_by("-id")[0:3]
    other_products = Product.objects.exclude(section__startswith='smartphones').order_by("-id")[0:10]

    context = {
        'phones': phones,
        'other_products': other_products
    }
    return render(request, template_name, context)


def phones(request):
    template_name = 'app_eshop/smartphones.html'
    context = pagination( request, Product.objects.filter(section__startswith='smartphones').order_by("id"), 3)
    return render_to_response(template_name, context)


def cultural(request):
    template_name = 'app_eshop/cultural.html'
    context = pagination( request, Product.objects.filter(section__startswith='cultural').order_by("id"), 3)
    return render_to_response(template_name, context)


def miscellaneous(request):
    template_name = 'app_eshop/miscellaneous.html'
    context = pagination(request, Product.objects.filter(section__startswith='miscellaneous').order_by("id"), 3)
    return render_to_response(template_name, context)


def phone(request, slug):
    template = 'app_eshop/product_detail.html'
    print('phone view:')
    #page_number = request.GET.get('page')

    if 'cart' in request.session:
        print(request.session['cart'])

    if request.method == 'POST':
        print('POST:', request.POST)
        product_get = get_object_or_404(Product, slug=slug)

        if 'merchandise_id' in request.POST:
            print('product to cart')
            if not ('cart' in request.session):
                request.session['cart'] = []
            product_to_cart = {'id': product_get.id,
                               'name': product_get.name,
                               'description': request.POST['description'],
                               'quantity': request.POST['merchandise_id']
                               }
            cart_current = request.session['cart']
            cart_current.append(product_to_cart)
            request.session['cart'] = cart_current
            return redirect(reverse('phone', args=[slug]))

        print('product show')
        #form=request.POST
        form = ReviewForm(request.POST)

        print(form.is_valid())

        review = Review(product=product_get,
                        name=form.cleaned_data['name'],
                        text=form.cleaned_data['text'],
                        rating=form.cleaned_data['rating'])
        review.save()
        return redirect(reverse('phone', args=[slug]))
    else:
        # pprint([i for i in dir(request) if not i.startswith('_')])
        form = ReviewForm

        phone_get = Product.objects.get(slug=slug)
        phone_detailed = Phone.objects.get(product_id=phone_get.id)

        context = {
            'form': form,
            'phone': phone_get,
            'detailed': phone_detailed,
        }
        return render(request, template, context)


def accessories(request):
    template_name = 'app_eshop/accessories.html'
    context = {}
    return render(request, template_name, context)


def product(request, slug):
    template = 'app_eshop/product_detail.html'

    if request.method == 'POST':
        print('POST:', request.POST)
        return redirect(reverse('phone', args=[slug]))
    else:
        # pprint([i for i in dir(request) if not i.startswith('_')])
        context = {
            'phone': Product.objects.get(slug=slug)
        }
        return render(request, template, context)


def cart(request):
    template = 'app_eshop/cart.html'
    if not ('cart' in request.session):
        request.session['cart'] = []
    cart_current = request.session['cart']
    cart_optimize = []

    for product in cart_current:
        match = False
        for product_was in cart_optimize:
            if product['id'] == product_was['id']:
                match = True
        if match:
            continue
        for product_cmp in cart_current[cart_current.index(product)+1:]:
            if product['id'] == product_cmp['id']:
                product['quantity'] = int(product['quantity']) + int(product_cmp['quantity'])
        cart_optimize.append(product)

    pprint(cart_optimize)

    context = {
        'products': cart_optimize
    }
    return render(request, template, context)

