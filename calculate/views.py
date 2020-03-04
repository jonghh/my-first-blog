from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import *
import re
# from konlpy.tag import Kkma
from collections import Counter

def calculate(request):
    # return HttpResponse('<h1>hello</h1>')
    result = ""
    if request.method == "GET":
        pass
    elif request.method == "POST":
        number1 = request.POST['number1']
## 직접인용 술어부 찾기
        regex1 = re.compile('\"고 \w+[다].')
        regex2 = re.compile('\"라고 \w+[다].')
        findings1 = regex1.findall(number1)
        findings2 = regex2.findall(number2)
        result = findings1 + findings2
## 주어 찾기
        #regex = re.compile("\w+[가이는은] ")
        #findings = regex.findall(number1)
        #result =[]
        #for word in findings:
        #    word = re.sub('[가이은는] ', '', word)
        #    result.append(word)
## 명사 빈도 분석기
        # tagger = Kkma()
        # nouns = tagger.nouns(number1)
        # count = Counter(nouns)
        # result = count.most_common(100)
    else:
            result = "nothing"
    return render(request, 'calculate/calculate.html', {'result':result})
