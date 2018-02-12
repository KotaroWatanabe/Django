from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render # ’Ç‰Á‚·‚é


def hello_world(request):
    return HttpResponse('Hello World!')
    
def hello_template(request):
    return render(request, 'index.html')
    
def hello_template2(request):
    return render(request, 'index2.html')
    
