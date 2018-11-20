import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# 하나의 모델 클래스는 데이터베이스에서 하나의 테이블에 해당하며 각각 클래스 변수는 필드타입에 맞는 클래스 객체를 생성하여 할당
class Question(models.Model):
    # 클래스 인스턴스 변수
    question_text = models.CharField(max_length=200)    # 필드 인스턴스의 이름은 데이터베이스의 칼럼 이름으로 쓰인다
    pub_date = models.DateTimeField('date published')

    # 클래스 메서드
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    #foreignkey로 묶여있을 경우 연쇄 삭제
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

