from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from .models import Quiz, Question


# Create your views here.
class IndexView(TemplateView):
    template_name = 'quiz/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quizzes'] = Quiz.objects.all()
        return context

class QuizDetailView(DetailView):
    template_name = 'quiz/detail.html'
    model = Quiz
    context_object_name = 'quiz'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quiz = self.object
        context['q1'] = quiz.questions.first()
        return context

class QuestionDetailView(DetailView):
    template_name = 'quiz/question-detail.html'
    model = Question
    context_object_name = 'question'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quiz'] = Quiz.objects.get(pk=self.kwargs.get('quiz_pk'))
        next_question = self.object.next_question()
        context['next_question'] = next_question
        context['is_final_question'] = next_question is None 
        return context