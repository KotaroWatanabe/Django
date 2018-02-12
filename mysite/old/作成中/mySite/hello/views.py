from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render # ’Ç‰Á‚·‚é



from . import forms


def hello_forms(request):
    form = forms.HelloForm(request.GET or None)
    if form.is_valid():
        message = 'sauccess'
    else:
        message = 'misssssss'
    d = {
        'form': form,
        'message': message,
    }
    return render(request, 'forms.html', d)
    ##############################################
def hello_forms2(request):
    d = {
        'form': forms.SampleForm(),
    }
    return render(request, 'form_samples.html', d)