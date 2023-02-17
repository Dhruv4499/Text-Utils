from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def aboutus(request):
    s = ['''<a href="/">back</a>''']
    return HttpResponse(s)
def contactus(request):
    s = ['''<a href="/">back</a>''']
    return HttpResponse(s)
def analyze(request):
    dummyText = request.POST.get('text','default')

    removepunc = request.POST.get('removepunc','off')
    uppercase = request.POST.get('uppercase','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcounter = request.POST.get('charcounter','off')

    if (removepunc == 'on'):
        Punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed='' 
        for char in dummyText:
            if char not in Punctuations:
                    analyzed = analyzed + char
        params = {'purpose':'Remove Punctuations','analyze_text':analyzed}
        dummyText = analyzed

    if (uppercase == 'on'):
        analyzed=''
        for char in dummyText:
            analyzed = analyzed + char.upper()
        dummyText = analyzed
        params = {'purpose':'Change to uppercase','analyze_text':analyzed}

    if (newlineremover == 'on'):
        analyzed=''
        for char in dummyText:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        params = {'purpose':'New Line Remover','analyze_text':analyzed}
        dummyText = analyzed

    if (extraspaceremover == 'on'):
        analyzed=''
        for index,char in enumerate(dummyText):
            if not(dummyText[index] == " " and dummyText[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Extra Space Remover','analyze_text':analyzed}
        dummyText = analyzed
        
    if (removepunc != 'on'and uppercase != 'on'and newlineremover != 'on'and extraspaceremover != 'on'):
        return HttpResponse("Please Select ay operation and try again")

    return render(request, 'analyze.html', params)