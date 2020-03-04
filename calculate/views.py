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
        number1 = number1.replace('”', '"')
        regex1 = re.compile('\"고 \w+[다].')
        regex2 = re.compile('\"고 \w+ \w+[다].')
        regex3 = re.compile('\"고 \w+ \w+ \w+[다].')
        regex4 = re.compile('\"라고 \w+[다].')
        regex5 = re.compile('\"라고 \w+ \w+[다].')
        regex6 = re.compile('\"라고 \w+ \w+ \w+[다].')
        regex7 = re.compile('\"이라고 \w+[다].')
        regex8 = re.compile('\"이라고 \w+ \w+[다].')
        regex9 = re.compile('\"이라고 \w+ \w+ \w+[다].')
        regex10 = re.compile('\"며 \w+[다].')
        regex11 = re.compile('\"며 \w+ \w+[다].')
        regex12 = re.compile('\"며 \w+ \w+ \w+[다].')
        regex13 = re.compile('\"라며 \w+[다].')
        regex14 = re.compile('\"라며 \w+ \w+[다].')
        regex15 = re.compile('\"라며 \w+ \w+ \w+[다].')
        regex16 = re.compile('\"이라며 \w+[다].')
        regex17 = re.compile('\"이라며 \w+ \w+[다].')
        regex18 = re.compile('\"이라며 \w+ \w+ \w+[다].')
        findings1 = regex1.findall(number1)
        findings2 = regex2.findall(number1)
        findings3 = regex3.findall(number1)
        findings4 = regex4.findall(number1)
        findings5 = regex5.findall(number1)
        findings6 = regex6.findall(number1)
        findings7 = regex7.findall(number1)
        findings8 = regex8.findall(number1)
        findings9 = regex9.findall(number1)
        findings10 = regex10.findall(number1)
        findings11 = regex11.findall(number1)
        findings12 = regex12.findall(number1)
        findings13 = regex13.findall(number1)
        findings14 = regex14.findall(number1)
        findings15 = regex15.findall(number1)
        findings16 = regex16.findall(number1)
        findings17 = regex17.findall(number1)
        findings18 = regex18.findall(number1)
        result = findings1+findings2+findings3+findings4+findings5+findings6+findings7+findings8+findings9+findings10+findings11+findings12+findings13+findings14+findings15+findings16+findings17+findings18

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
