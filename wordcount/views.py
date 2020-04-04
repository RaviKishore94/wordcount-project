#from django.http import HttpResponse #for returning a simplt http response
from django.shortcuts import render #for returning a user defined template

def homepage(request):
    #return HttpResponse("<h1>Hello</h1>")
    return render(request, 'home.html', {'UserName':'Ravi'}) #passing a dictionary to home.html for interpolations

def countpage(request):
    input_text = request.GET['fulltext'] #getting the query string
    words = input_text.split()
    words_count = {}
    for w in words:
        words_count.setdefault(w, 0)
        words_count[w] += 1
    word_count = sorted(words_count.items(), key = lambda x:x[1], reverse=True)
    return render(request, 'count.html', {'fulltext': input_text, 'wordcount': len(words), 'eachwordcount': word_count})
