from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render # �ǉ�����


def hello_get_query(request):
    d = {
        'your_name': request.GET.get('your_name')
    }
    return render(request, 'get_query.html', d)