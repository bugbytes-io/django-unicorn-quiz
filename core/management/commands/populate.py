from django.core.management.base import BaseCommand

from core.models import Quiz, Question, Choice


class Command(BaseCommand):
    help = 'Generates testing data for development'

    def handle(self, *args, **kwargs):
        quiz = Quiz.objects.get_or_create(name='Python Data Types')[0]

        questions = [
            Question(quiz=quiz, text='Which of these data types is NOT mutable?', order=1),
            Question(quiz=quiz, text='Which data type is a numeric type?', order=2),
            Question(quiz=quiz, text='Which data type is NOT ordered?', order=3),
        ]

        if Question.objects.count() == 0:
            Question.objects.bulk_create(questions)

        questions = Question.objects.all()

        # create answers
        q1_choices = [
            Choice(question=questions[0], text='List', is_correct=False),
            Choice(question=questions[0], text='Tuple', is_correct=True),
        ]
        
        q2_choices = [
            Choice(question=questions[1], text='Float', is_correct=True),
            Choice(question=questions[1], text='String', is_correct=False),
        ]
        
        q3_choices = [
            Choice(question=questions[2], text='Tuple', is_correct=False),
            Choice(question=questions[2], text='Set', is_correct=True),
        ]

        if Choice.objects.count() == 0:
            Choice.objects.bulk_create(q1_choices + q2_choices + q3_choices)
        