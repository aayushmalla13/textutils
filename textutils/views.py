# I have created this file - Harry video #17
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")


def ex1(request):
    sites = ['''For Entertainment youtube video''',
             '''For Interaction Facebook''',
             '''For Insight   Ted Talk''',
             '''For Internship   Intenship''',
             ]
    return HttpResponse((sites))

def analyze(request):
    #Get Text
    djtext= request.POST.get('text','default')
    #get checkbox list
    removepunc= request.POST.get('removepunc','off')
    tocapital=request.POST.get('tocapital','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    analyzed =''
    purpose = ''

    if(removepunc=='on'):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        purpose = purpose + 'remove punctuation'
        djtext = analyzed

    if(tocapital=='on'):
        analyzed=djtext.upper()
        djtext=analyzed
        purpose = purpose + 'Capitalization'

    if(newlineremover=='on'):
        purpose= purpose + 'New Line remover'
        temp=''
        for char in djtext:
             if char != '\n' and char !='\r':
                 temp=temp+char
        analyzed=temp
        djtext=analyzed

    if(extraspaceremover=='on'):
        purpose=purpose+' extraspaceremover'
        tempr=''
        for index,char in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                tempr=  tempr + char
        analyzed=tempr
        djtext=analyzed

    params= {'purpose':purpose,'analyzed_text':analyzed}
    return render(request,'analyze.html',params)


def contactus(request):

    return render(request,'contactus.html')

def aboutus(request):
    return render(request,'aboutus.html')




