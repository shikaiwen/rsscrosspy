from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.http import *
from django.template import loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Question
import os
# from os import *
import json


def index(request):
    latest_question_list = Question.objects.order_by("pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

@csrf_exempt
def wordexists(request, user_id):

    word = request.GET['w']
    resp = {"code": 1, "exists": 0}

    file = os.path.dirname(__file__) + "/notes/" + user_id

    with open(file, "r", encoding="utf-8") as fo:
        list = fo.readlines()
        list = list[1:]
        contains = [cur for cur in list if json.loads(cur)['word'] == word]
        resp['exists'] = 0 if len(contains) == 0 else 1

    return JsonResponse(resp)


# save words from chrome's kquery
def saveword(request):
    word = request.GET['w'];

    dict = {"code": "1", "msg": 1}

    # word(单词) jm(英文假名) roma(罗马假名) sd(声调) fyf(说明内容，用换行符号分割)
    content = {
        "word": "忍ぶ",
        "jm": "sinobu",
        "sd": "1",
        "fyf": "【自动词・五段/一类】\n（1）上，登，攀登。\n（2）逆流而上，上溯。"
    }

    file = os.path.dirname(__file__) + "/notes/" + "me"

    with open(file, "a") as fo:
        list = fo.readlines()
        contains = [cur for cur in list if json.load(cur)['word'] == word]
        if len(contains) == 0:
            jsonstr = json.dumps(content)
            jsonstr += "\n"
            fo.write(jsonstr)
        else:
            dict['st':0, "msg", "该单词已经保存"]
    resp = JsonResponse(dict)
    return resp


# remove words from notebook
def removeword(request):
    word = request.GET['w'];
    dict = {"st1": "1", "msg": "ok"}
    resp = JsonResponse(dict)

    return resp


# return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're loooking at the results of question %s."


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
