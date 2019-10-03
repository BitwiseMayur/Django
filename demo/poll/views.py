from django.shortcuts import render
from poll.models import *

# Create your views here.
def index(request):
    questions = Question.objects.all()

    context = {'title': 'polls', 'questions': questions}

    return render(request, 'poll/index.html', context)

def detail(request, id):
    question = Question.objects.get(pk=id)

    context = {'question': question}

    return render(request, 'poll/detail.html', context)