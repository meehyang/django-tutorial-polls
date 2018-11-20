"""
WSGI config for poll project.

내 프로젝트를 돕는 웹서버와 웹서버 게이트웨이 인터페이스 호환을 위한 시작점.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'poll.settings')

application = get_wsgi_application()
