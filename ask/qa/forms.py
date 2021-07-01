from django import forms
from django.contrib.auth.models import User

from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea())

    def save(self):
        return Question.objects.create(
            title=self.cleaned_data['title'],
            text=self.cleaned_data['text'],
            author=User.objects.first()
        )


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea())
    question = forms.ModelChoiceField(Question.objects.all())

    def __init__(self, question_id, data=None):
        self.base_fields['question'].initial = question_id
        super(AnswerForm, self).__init__(data)

    def save(self):
        return Answer.objects.create(
            text=self.cleaned_data['text'],
            question=self.cleaned_data['question'],
            author=User.objects.first()
        )
