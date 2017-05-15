from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.http import Http404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ','.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(request,'polls/index.html',context)
    # return HttpResponse('hello,world,you are the polls index.')

def detail(request,question_id):
    try:
        question = Question.objects.get(pk=int(question_id))
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return HttpResponse(request,'polls/detail.html',{ 'question':question })

def results(request,question_id):
    return HttpResponse('You are looking at the result of question %s.' % question_id)

def vote(request,question_id):
    return HttpResponse('You are voting on question %s.'%question_id)
# Create your views here.
