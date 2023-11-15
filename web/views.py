from django.shortcuts import render


# Create your views here.
def welcome_view(request):
    content = {
        "greetings": "Добро пожаловать в наш интренет-магазин!"
    }
    return render(request, 'web/base.html', context=content)


def contacts(request):
    contact = {
        'name': 'Виртуальный магазинчик',
        'Email': 'hello@virtualmart.com',
        'adress': 'Ул. Виртуальная, д. 456, Город, Страна',
    }
    return render(request, 'web/contacts.html', context=contact)
