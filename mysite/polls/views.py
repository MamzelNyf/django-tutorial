from django.http import HttpResponseRedirect

# from django.http import HttpResponse
# from django.template import loader
# from django.shortcuts import render
# from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

# Create your views here.

# def index(request):
#     #return HttpResponse('Hello, world. You are at the polls index.')
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     ## 1st display : get the last 5 questions and display them separated by a coma
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)

    
#     ## 2nd display: loads the template called polls/index.html and passes it a context
#     ## context is a dictionary mapping template variable names to Python objects
#     # template = loader.get_template('polls/index.html')
#     # context = {
#     #     'latest_question_list': latest_question_list,
#     # }
#     # return HttpResponse(template.render(context, request))

#     ## 3rd: shorcut to load a template, fill a context and return an HttpResponse object with the 
#     ## result of the rendered template.
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#     ##  render() function takes the request object as its first argument, a template name as its 
#     ## second argument and a dictionary as its optional third argument. 
#     ## It returns an HttpResponse object of the given template rendered with the given context.

# def detail(request, question_id):
#     #return HttpResponse("You're looking at question %s." % question_id) 
#     ## 
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question': question})

#     ## shorcut to raise the Http404 exception if a question with the requested ID doesn’t exist.
#     ## The get_object_or_404() function takes a Django model as its first argument and an arbitrary 
#     ## number of keyword arguments, which it passes to the get() function of the model’s manager.
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question' : question})


# def results(request, question_id):
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question.id)
#     return render(request, 'polls/results.html', {'question' : question})

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

#  DetailView generic view expects the primary key value captured from the URL
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # request.POST is a dictionary-like object that lets you access submitted data by key name. POST values are always strings.
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })  
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        # reverse() helps avoid having to hardcode a URL in the view function. 