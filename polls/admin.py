from django.contrib import admin
from .models import Question

# Register your models here.
# Question object 가 admin interface 를 가지고 있다는 것을 admin에게 알려줘야함
admin.site.register(Question)
