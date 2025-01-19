from django.shortcuts import render
from .models import Lecture

def homework(request):
    homework = Lecture.objects.all()  # 모든 강의 데이터 가져오기
    context = {"homework":homework}
    return render(request, 'lectures/homework.html', context)

