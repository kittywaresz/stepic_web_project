from django import forms
from django.contrib.auth.models import User

from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea())

    def __init__(self, user=None, data=None):
        self._user = user
        super(AskForm, self).__init__(data)

    def save(self):
        return Question.objects.create(
            title=self.cleaned_data['title'],
            text=self.cleaned_data['text'],
            author=self._user
        )


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea())
    question = forms.ModelChoiceField(Question.objects.all())

    def __init__(self, question_id=None, user=None, data=None):
        self.base_fields['question'].initial = question_id
        self._user = user
        super(AnswerForm, self).__init__(data)

    def save(self):
        return Answer.objects.create(
            text=self.cleaned_data['text'],
            question=self.cleaned_data['question'],
            author=self._user
        )


class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def save(self):
        return User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
