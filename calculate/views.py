from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import *
from re
# from konlpy.tag import Kkma
from collections import Counter

def calculate(request):
    # return HttpResponse('<h1>hello</h1>')
    result = ""
    if request.method == "GET":
        pass
    elif request.method == "POST":
        number1 = request.POST['number1']
        regex = re.compile("\w+[가이는은] ")
        findings = regex.findall(number1)
        result =[]
        for word in findings:
            word = re.sub('[가이은는] ', '', word)
            result.append(word)
"""
        tagger = Kkma()
        nouns = tagger.nouns(number1)
        count = Counter(nouns)
        result = count.most_common(100)
"""
    else:
            result = "nothing"
    return render(request, 'calculate/calculate.html', {'result':result})
