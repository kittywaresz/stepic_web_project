from django.shortcuts import render, get_object_or_404

from .models import Question
from .utils import paginate


def index(request, *args, **kwargs):
    page = request.GET.get('page', default=1)

    return render(
        request,
        template_name='qa/index.html',
        context={
            'page': paginate(Question.objects.new(), limit=10, page=page)
        }
    )


def popular(request, *args, **kwargs):
    page = request.GET.get('page', default=1)

    return render(
        request,
        template_name='qa/popular.html',
        context={
            'page': paginate(Question.objects.popular(), limit=10, page=page)
        }
    )


def question(request, *args, **kwargs):
    pk = kwargs.get('pk', 0)
    object_ = get_object_or_404(Question.objects, pk=pk)

    return render(
        request,
        template_name='qa/question.html',
        context={
            'object': object_
        }
    )
