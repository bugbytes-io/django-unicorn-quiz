from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('quiz/<int:pk>', views.QuizDetailView.as_view(), name='quiz-detail'),
    path(
        'quiz/<int:quiz_pk>/question/<int:pk>/', 
        views.QuestionDetailView.as_view(),
        name='question-detail'
    ),
]