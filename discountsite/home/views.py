from django.shortcuts import render
from django.http import HttpResponse
import discountsite.common

def index(request):
    context = {}

    if request.method == 'POST':
        search_input = request.POST.get('search input', None)
        return render(request, 'home/index.html', context)
    else:
        return render(request, 'home/index.html', context)
