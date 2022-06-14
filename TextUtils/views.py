from django.http import HttpResponse
from django.shortcuts import render

def index(request):


    return render(request,'index.html')


def analyzer(request):
    djtext = request.POST.get('text','default')
    checkbox=request.POST.get('removepunc','off')
    capfirst = request.POST.get('capfirst', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount= request.POST.get('charcount', 'off')

    if checkbox=='on':
        punctuation='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for char in djtext:
            if char not in punctuation:
                analyzed=analyzed + char
        params={
            "purpose":'Removed Punctuation',
            "analyzer":analyzed,
            'count': "Default"

        }
        djtext = analyzed
        # return render(request, 'analyzer.html', params)


    if capfirst=='on':
        analyzed=""
        for char in djtext:
            analyzed= analyzed+char.upper()
        params={
            "purpose":'Capitalized the letter',
            "analyzer":analyzed,
            'count': "Default"

        }
        djtext = analyzed
        # return render(request,'analyzer.html',params)

    if newlineremove=='on':
        analyzed=""
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed=analyzed+char
        

        params={
            "purpose":'Capitalized the letter',
            "analyzer":analyzed,
            'count': "Default"

        }
        djtext = analyzed
        # return render(request,'analyzer.html',params)




    if spaceremove=='on':
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char

        params={
            "purpose":'Removed the extraspaces ',
            "analyzer":analyzed,
            'count': "Default"


        }
        djtext=analyzed
        # return render(request,'analyzer.html',params)

    if charcount=='on':
        counter=""
        for char in djtext:
            if char!=" ":
                counter=counter+char
                count=len(counter)
        params={
            "purpose": 'Removed the extraspaces ',
            "analyzer": analyzed,
            'count':count

        }
    if (checkbox!='on'and capfirst!='on' and newlineremove!='on' and spaceremove!='on' and charcount!='on'):
        return HttpResponse("Please select the checkbox and try again")



    return render(request, 'analyzer.html', params)










