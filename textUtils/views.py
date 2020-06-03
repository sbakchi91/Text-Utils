# I have created this file - VLAD
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("HOME")


def navi(request):
    return HttpResponse('''<h1>__________________________________Personal Navigator_________________________________</h1><br>
    <h1>For Best Motivational Books click the below link</h1>
    <h2><a href = "https://www.lifehack.org/842960/motivational-books">Best Motivational Books</a></h2><br>
    <h1>For Best Motivational Movies click the below link</h1>
    <h2><a href = "https://www.lifehack.org/articles/lifestyle/35-inspirational-movies-that-will-change-your-life.html">
    Best Motivational Movies</a></h2><br>
    <h1>For Best Motivational Quotes click the below link</h1>
    <h2><a href = "https://www.lifehack.org/508435/50-highly-motivational-quotes-prepare-you-for-2017">
    Best Motivational Quotes</a></h2>''')

def textFile(request):
    with open("D:\/course.txt") as f:
        a = f.read()
        return HttpResponse(a)


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Create the Checkbox
    removepunc = request.POST.get('removepunc', 'off')
    fulcaps = request.POST.get('fulcaps', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')

    new = djtext

    if removepunc == "on":
        analyzed = ""
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^`{|}~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        # var = {'purpose': 'Removed Punctuations', 'Analyzed_text': analyzed}
        new = analyzed
        # return render(request, 'analyze.html', var)

    if fulcaps == "on":
        analyzed = ""
        for char in new:
            analyzed = analyzed + char.upper()
        # var = {'purpose': 'UPPER CASE ALPHABET', 'Analyzed_text': analyzed}
        new = analyzed
        # return render(request, 'analyze.html', var)

    if newlineremover == "on":
        analyzed = ""
        for char in new:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        new = analyzed
        # var = {'purpose': 'New Lines are Removed', 'Analyzed_text': new}
        # return render(request, 'analyze.html', var)

    if spaceremove == "on":
        analyzed = ""
        for index, char in enumerate(new):
            if not(new[index] == " " and new[index+1] == " "):
                analyzed = analyzed + char
        new = analyzed

    var = {'purpose': 'Removed necessary conditions mentioned By User', 'Analyzed_text': new}

    if removepunc == "on" or fulcaps == "on" or spaceremove == "on" or newlineremover == "on":
        return render(request, 'analyze.html', var)

    else:
        return HttpResponse("Error")


def about(request):
    return HttpResponse("Yoo Cool!!! <a href = '/'>Back</a>")
