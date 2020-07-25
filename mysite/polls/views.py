from django.http import HttpResponse

#from django.template import loader
#from django.shortcuts import render
# from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Question

# Create your views here.

def index(request):
    #return HttpResponse('Hello, world. You are at the polls index.')
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    ## 1st display : get the last 5 questions and display them separated by a coma
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    
    ## 2nd display: loads the template called polls/index.html and passes it a context
    ## context is a dictionary mapping template variable names to Python objects
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    ## 3rd: shorcut to load a template, fill a context and return an HttpResponse object with the 
    ## result of the rendered template.
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    ##  render() function takes the request object as its first argument, a template name as its 
    ## second argument and a dictionary as its optional third argument. 
    ## It returns an HttpResponse object of the given template rendered with the given context.

def detail(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id) 
    ## 
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})

    ## shorcut to raise the Http404 exception if a question with the requested ID doesn’t exist.
    ## The get_object_or_404() function takes a Django model as its first argument and an arbitrary 
    ## number of keyword arguments, which it passes to the get() function of the model’s manager.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)   