"""poll URL Configuration

프로젝트 poll의 장고 URL 선언들. 장고 프레ㅣㅁ워크 안에영향을 받는 컨텐츠들의 집합.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path


# http://pythonstudy.xyz/python/article/311-URL-%EB%A7%A4%ED%95%91 매핑 관련 참고 사이트
# 하나의 프로젝트에 여러 django app이 존재한다면 프로젝트의 main urls.py에서 모든 매핑을 관리하기보다는 각각의 app의 urls.py에서 매핑을 관리하고
# 메인프로젝트 url.py 에서는 각각의 앱으로 매핑을 위탁 처리하는 방식을 주로 사용함
urlpatterns = [
    # polls 로 시작되는 url은 polls.urls 안에 있는 매핑을 사용하겠다는 의미
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

# include() 함수는 다른 URL환경을 참조하는 것을 허락해준다. 장고가 해당 함수를 만나면 일치하는 URL을 잘라내고 추가적 처리를 위해 url에 포함된 나머지 문자열을 보낸다
# url을 쉽게 매칭하고 운용할 수 있게 해줌. URLconf(polls/urls.py) 에 위치하게 되면 /polls/ /fun_polls/ /content/polls/ 등 어디에 있더라도 작동 가능
# include()는 어떤 url 패턴이나 다 사용 가능함. admin.site.urls 는 유일한 예외

