from django.http import HttpResponse
from django.template import loader


def index(request, *args, **kwargs):
    # print('GET', request.GET)
    # print('POST', request.POST)
    # print('COOKIES', request.COOKIES)
    # print('FILES', request.FILES)
    # print('META', request.META)

    template = loader.get_template('index.html')

    return HttpResponse(template.render(
        {
            'meta': request.META
        },
        request)
    )
