import urllib.parse
from pprint import pprint

from django.core.paginator import Paginator
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.urls import reverse

from .models import Product, Review  # app_eshop
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
        prod = get_object_or_404(Product, slug=slug)

        if 'merchandise_id' in request.POST:
            print('product to cart')
            if not ('cart' in request.session):
                request.session['cart'] = []
            busket = request.session['cart']
            product_to_cart = {'product': prod.id,
                               'quantity': request.POST['merchandise_id']
                               }
            busket.append(product_to_cart)

            request.session['cart'] = busket
            return redirect(reverse('phone', args=[slug]))
        print('product show')

        #form=request.POST

        #print(prod.id)
        form = ReviewForm(request.POST)
        #for field in form:
        #    print(field)
        print(form.is_valid())

        review = Review(product=prod, name=form.cleaned_data['name'], text=form.cleaned_data['text'], rating=form.cleaned_data['rating'])
        review.save()
        return redirect(reverse('phone', args=[slug]))
    else:
        # pprint([i for i in dir(request) if not i.startswith('_')])
        form = ReviewForm
        context = {
            'form': form,
            'phone': Product.objects.get(slug=slug)
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
    busket = request.session['cart']
    #product_to_cart = {'product': prod.id,
    #                   'quantity': request.POST['merchandise_id']
    #                   }
    #busket.append(product_to_cart)

    request.session['cart'] = busket
    context = {}
    return render(request, template, context)

