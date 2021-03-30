from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import TestForm

from .models import ProteinShake


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {'form': TestForm()}
    return render(request, 'protein/index.html', context)

def shake(request, shake_name):
    shake = get_object_or_404(ProteinShake, name=shake_name)
    return render(request, 'protein/shake.html', {'shake': shake})

def shakes(request):
    search = ""
    searched = False;
    if request.GET.get('search', False):
        shakes = ProteinShake.objects.filter(name__contains=request.GET.get('search', False)).order_by('opinion')
        search = request.GET.get('search', False)
        searched = True
    else:
        shakes = ProteinShake.objects.order_by('opinion')

    return render(request, 'protein/list.html', {'shakes': shakes, 'searched': searched, 'search': search})
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))