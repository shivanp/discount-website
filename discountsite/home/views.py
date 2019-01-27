from django.shortcuts import render
from django.http import HttpResponse
import discountsite.common

def index(request):
    context = {}
    return render(request, 'home/index.html', context)
