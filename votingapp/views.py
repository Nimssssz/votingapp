from django.shortcuts import render
from django.http import HttpResponse

arr = ['Java', 'Python', 'Cplusplus', 'C', 'DotNET', 'JavaScript', 'PHP', 'Swift', 'SQL', 'Ruby', 'Delphi', 'Objective-C', 'Go', 'Assemblylanguage', 'VisualBasic', 'D', 'R', 'Perl', 'MATLAB']

globalcnt = dict()

def index(request):
    dc = {
        "arr" : arr,
    }
    return render(request, 'index.html', context = dc)

def getquery(request):
    q = request.GET['languages']  
    if q in globalcnt:
        globalcnt[q] = globalcnt[q]+1
    else:
         globalcnt[q]=1
    dc = {
        "arr":arr,
        "globalcnt":globalcnt,
    }
    return render(request ,'index.html', context=dc)

def sortdata(request):
    global globalcnt
    globalcnt = dict(sorted(globalcnt.items(), key=lambda x:x[1], reverse=True))
    dc = {
        "arr" : arr,
        "globalcnt" : globalcnt,
    }
    return render(request, 'index.html', context = dc)
