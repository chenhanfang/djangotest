from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Question,Choice
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
#
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ','.join([q.question_text for q in latest_question_list])
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(output)
    # return render(request,'polls/index.html',context)
    # return HttpResponse('hello,world,you are the polls index.')

def index(request):#####另一种方法写index
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list,
    }
    # return HttpResponse(template.render(context,request))####利用template
    return render(request,'polls/index.html',context)

# def detail(request,question_id):
#     try:
#         question = Question.objects.get(pk=int(question_id))
#     except Question.DoesNotExist:
#         raise Http404('Question does not exist')
#     return render(request,'polls/detail.html',{ 'question':question })

def detail(request,question_id):####另一种方法写detail,比较方便的方法写404页面
    question = get_object_or_404(Question, pk = question_id)
    return render(request,'polls/detail.html',{ 'question':question })

def results(request,question_id):
    # return HttpResponse('You are looking at the result of question %s.' % question_id)
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':'You did not select a choice.',
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
    # return HttpResponse('You are voting on question %s.'%question_id)
# Create your views here.
