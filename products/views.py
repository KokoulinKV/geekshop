from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'products.html')


def test(request):
    context = {
        'title': 'geekshop',
        'user': 'Ivan',
        'description': 'Добро пожаловать в GeekShop!',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00 руб.'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00 руб.'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00 руб.'}
        ],
        'promotion': True,
        'products_of_promotion': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00 руб.'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00 руб.'}
        ]
    }

    return render(request, 'test.html', context)