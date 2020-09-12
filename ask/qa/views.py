from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index(request, *args, **kwargs):
    return HttpResponse("Hello, world. You're at the polls index.")
