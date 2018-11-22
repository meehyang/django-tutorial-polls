from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Question

# Create your views here.
# 장고는 기존 쿼리스트링 방식에 비해 /newsarchive/<year>/<month> 같은 간결한 URL 패턴을 사용한다.
# url에서 view 를 가져오기 위해 django는 'URLconfs' 라는 것을 사용한다. URLconfs는 URL과 view를 매핑해준다.

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]   # list를 가져오기 위한 query 실행
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# 좀 더 짧은 방식으로 정의할 수 있다.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # DB model 객체에서 반환하는 값이 없을 때의 예외처리
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')

    # 위 내용을 1줄로 줄일수도 있다.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "현재 질문 '%s'에 대한 결과를 보고 계십니다."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("질문 '%s'에 투표하셨습니다." % question_id)
