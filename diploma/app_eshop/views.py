from pprint import pprint

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Product, Review, Phone, Cultural, Miscellaneous, Section, Cart, ProductsInCart
from .forms import ReviewForm
from .functions import pagination, cart_parse, drop_menu

from app_articles.models import Article


def main(request):
    template_name = 'index.html'

    section_name = Section.objects.filter(location='section 1')[0]
    phones = Product.objects.filter(section__name=section_name).order_by("-id")[0:3]

    other_products = Product.objects.exclude(section__name=section_name).order_by("-id")[0:10]

    articles_phones = Article.objects.filter(section__name=section_name).order_by('published_at')[0:3]
    articles_other = Article.objects.exclude(section__name=section_name).order_by('published_at')[0:3]

    # for article in articles_phones:
    #     print('article:', article.section)
    #
    #     for prod in article.products.all():
    #         print('product:', prod.name)

    context = {
        'phones': phones,
        'other_products': other_products,
        'articles_phones': articles_phones,
        'articles_other': articles_other
    }
    context.update({'drop_menu': drop_menu})
    return render(request, template_name, context)


def gadgets(request, slug):
    template_name = f'app_eshop/sections.html'
    menu_section = Section.objects.get(slug=slug)
    context = pagination(request, Product.objects.filter(section__name=str(menu_section)).order_by("id"), 3)
    context.update({'title': menu_section})
    context.update({'drop_menu': drop_menu})
    return render(request, template_name, context)


def accessories(request):
    template_name = 'app_eshop/accessories.html'
    context = {
        'drop_menu': drop_menu
    }
    return render(request, template_name, context)


def product(request, slug):
    template = 'app_eshop/product_detail.html'
    name_url = request.resolver_match.url_name
    print('name_url:', name_url)
    if request.method == 'POST':
        product_get = get_object_or_404(Product, slug=slug)
        if 'merchandise_id' in request.POST:
            if not ('cart' in request.session):
                request.session['cart'] = []
            product_to_cart = {'id': product_get.id,
                               'quantity': int(request.POST['merchandise_id']),
                               'price': product_get.price,
                               'name': product_get.name,
                               'description': request.POST['description']
                               }
            cart_current = request.session['cart']
            cart_current.append(product_to_cart)
            request.session['cart'] = cart_current
            if 'template' in request.POST:
                return redirect(reverse(name_url, args=[slug]))
            return redirect(reverse('index', args=[product_get.section.slug]))
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review(
                product=product_get,
                name=form.cleaned_data['name'],
                text=form.cleaned_data['text'],
                rating=form.cleaned_data['rating']
            )
            review.save()
        return redirect(reverse(name_url, args=[slug]))
    else:
        form = ReviewForm
        product_get = Product.objects.get(slug=slug)
        product_reviews = Review.objects.all().filter(product_id=product_get.id)
        section_name = Section.objects.get(name=product_get.section)

        try:
            if section_name.template_name == 'phone':
                product_detailed = Phone.objects.get(product_id=product_get.id)
            elif section_name.template_name == 'culture':
                product_detailed = Cultural.objects.get(product_id=product_get.id)
            elif section_name.template_name == 'miscellaneous':
                product_detailed = Miscellaneous.objects.get(product_id=product_get.id)
            else:
                product_detailed = ''
        except Exception:
            product_detailed = ''

        context = {
            'form': form,
            'product': product_get,
            'section_name': str(section_name),
            'product_template': f'app_eshop/{section_name.template_name}_detail.html',
            'reviews': product_reviews,
            'name_url': name_url,
            'detailed': product_detailed
        }
        context.update({'drop_menu': drop_menu})
        return render(request, template, context)


@login_required(login_url="/")
def cart(request):
    template = 'app_eshop/cart.html'
    if request.method == 'POST':
        order_cart = Cart.objects.create(
            user=User.objects.get(email=request.POST['user']),
            price=request.POST['price_common'],
            qty=request.POST['qty_common']
        )
        order_cart.save()
        for item in cart_parse(request.POST['products']):
            product_in_cart = ProductsInCart.objects.create(
                cart=order_cart,
                product=Product.objects.get(id=item['id']),
                quantity=item['qty']
            )
            product_in_cart.save()
        del request.session['cart']
        context = {
            'status': 'order send'
        }
        context.update({'drop_menu': drop_menu})
        return render(request, template, context)
    else:
        if not ('cart' in request.session):
            request.session['cart'] = []
        cart_current = request.session['cart']
        cart_optimize = []
        qty_common = 0
        price_common = 0

        for item in cart_current:
            match = False
            for product_was in cart_optimize:
                if item['id'] == product_was['id']:
                    match = True
            if match:
                continue
            for product_cmp in cart_current[cart_current.index(item)+1:]:
                if item['id'] == product_cmp['id']:
                    item['quantity'] = int(item['quantity']) + int(product_cmp['quantity'])
                item['description'] = item['description'][0:50]
            cart_optimize.append(item)
        print('cart')
        pprint(cart_optimize)
        for item in cart_optimize:
            qty_common += int(item['quantity'])
            price_common += int(item['price']) * int(item['quantity'])

        context = {
            'qty_common': qty_common,
            'price_common': price_common,
            'products': cart_optimize,
            'status': 'processing'
        }
        context.update({'drop_menu': drop_menu})
        return render(request, template, context)

