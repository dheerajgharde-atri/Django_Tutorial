from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latest_question_list': latest_question_list
    }
    # First way to implement
    # template = loader.get_template('polls/index.html')

    # return HttpResponse(template.render(context,request))

    # Shortcut
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)



def results(request, question_id):
    return HttpResponse("You are looking at results pf question {}".format(question_id))


def vote(request, question_id):
    return HttpResponse("You are voting on question {0}".format(question_id))