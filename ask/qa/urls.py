from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import (
    index,
    popular,
    question,
    ask,
    signup
)

urlpatterns = [
    path('', index, name='index'),
    path('popular/', popular, name='popular'),
    path('question/<int:pk>/', question, name='question'),
    path('ask/', ask, name='ask'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
