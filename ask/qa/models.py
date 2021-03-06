from django.contrib.auth.models import User
from django.db import models


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()

    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(
        User,
        null=False,
        on_delete=models.CASCADE
    )
    likes = models.ManyToManyField(
        User,
        related_name='liked_questions'
    )


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(
        Question,
        null=False,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        null=False,
        on_delete=models.CASCADE
    )
