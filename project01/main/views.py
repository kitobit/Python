from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = {
        'title': 'Главная',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }

    return render(request,'main/index.html',data)

def about(request):
    return render(request,'main/about.html')

def sum(request):

    a = 5
    b = 6
    sum1 = a + b

    data = {
        'title': 'Главная',
        'sum': sum1,
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request,'main/about.html',data)