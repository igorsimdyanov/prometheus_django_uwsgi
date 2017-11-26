from django.http import HttpResponse
from prometheus_client import Counter

c = Counter('hello_counter', 'Количество вызовов hello')


def hello(request):
    c.inc()
    return HttpResponse('Привет!')
