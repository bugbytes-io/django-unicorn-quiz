from django_unicorn.components import UnicornView
from core.models import Choice, Choice

class QuestionView(UnicornView):
    choice_pk = None
    choice_text = ''
    choices = None
    correct = None
    text_color = None

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)  # calling super is required
        self.qid = kwargs.get("qid")

    def hydrate(self):
        self.choices = Choice.objects.filter(question=self.qid).values('pk', 'text')
        print(self.choice_pk)

    def set_answer(self, choice_pk):
        self.correct = None
        self.choice_pk = choice_pk
        self.choice_text = [c['text'] for c in self.choices if c['pk']==choice_pk][0]
        self.set_class()
        
    def check_answer(self):
        if self.choice_pk is not None:
            self.correct = Choice.objects.get(pk=self.choice_pk).is_correct
            self.set_class()
        
    def set_class(self):
        if self.correct is None:
            self.text_color = ''
        else:
            if self.correct:
                self.text_color = 'text-success'
            else:
                self.text_color = 'text-danger'

    def clear(self):
        self.correct = None
        self.choice_pk = None
        self.choice_text = None
