from django.urls import path

from .views import (
    index,
    popular,
    question
)

urlpatterns = [
    path('', index, name='index'),
    path('popular/', popular, name='popular'),
    path('question/<int:pk>/', question, name='question'),
    # info: below not implemented
    path('new/', index, name='new'),
    path('ask/', index, name='ask'),
    path('login/', index, name='login'),
    path('signup/', index, name='signup'),
]
