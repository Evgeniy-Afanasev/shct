from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]



class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Снова отображаем страницу detail
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Ничего не выбрано!",
        })
    else:   
        selected_choice.votes += 1
        selected_choice.save()
        # Всегда возвращайте HttpResponseRedirect после успешной 
        # обработки POST. Это защищает от повторной отправки
        # сообщения при нажатии на кнопку "назад"
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))