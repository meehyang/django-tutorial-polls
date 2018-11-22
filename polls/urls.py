from django.urls import path

from . import views

app_name='polls'
# 만들어진 view들을 polls.urls 모듈에 path()를 메서드를 이용해 view들을 더해준다
urlpatterns = [
    # /polls/ 로 호출된 경우
    path('', views.IndexView.as_view(), name='index'),
    # /polls/5/ 형태로 호출된 경우
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
