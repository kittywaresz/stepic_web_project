from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import AskForm, AnswerForm, SignupForm
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

    if request.method == 'POST':
        form = AnswerForm(pk, request.user, request.POST)

        if form.is_valid():
            _ = form.save()

            return HttpResponseRedirect(
                reverse('question', kwargs={'pk': object_.pk})
            )
    else:
        form = AnswerForm(pk, request.user)

    return render(
        request,
        template_name='qa/question.html',
        context={
            'object': object_,
            'form': form
        }
    )


def ask(request, *args, **kwargs):
    if request.method == 'POST':
        form = AskForm(request.user, request.POST)

        if form.is_valid():
            object_ = form.save()

            return HttpResponseRedirect(
                reverse('question', kwargs={'pk': object_.pk})
            )
    else:
        form = AskForm(request.user)

    return render(
        request,
        template_name='qa/ask.html',
        context={
            'form': form
        }
    )


def signup(request, *args, **kwargs):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = SignupForm()

    return render(
        request,
        template_name='registration/signup.html',
        context={
            'form': form
        }
    )
