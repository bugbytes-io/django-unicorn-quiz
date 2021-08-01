from django.db import models
from django.urls import reverse

class Quiz(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=1000)
    order = models.SmallIntegerField() # could use AutoField() here

    class Meta:
        ordering = ('order',)

    def next_question(self):
        return Question.objects.filter(
            quiz=self.quiz, order__gt=self.order
        ).first()

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text