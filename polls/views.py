# from lib2to3.fixes.fix_input import context

from django.http import Http404
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.template import loader
from pywin.tools.browser import template

from polls.models import Question

#load template -> fill context -> return HttpResponse object
# dex(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# short cut in django

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):

    question = get_object_or_404(Question,pk=question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    return render(request, "polls/detail.html", {"question": question} )

def results(request, question_id):
    response = "You are looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)



