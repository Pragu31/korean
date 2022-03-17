from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sonyu_jin(request):
    return HttpResponse('south korean television series')