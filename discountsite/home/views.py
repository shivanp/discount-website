from django.shortcuts import render
from django.http import HttpResponse
import discountsite.common as com

def index(request):
    context = {}
    item = 'women shoes'
    master_array = com.asos.search(item) + com.uniqlo.search(item) + com.gap.search(item) + com.handm.search(item)
    return render(request, 'home/index.html', context)


def sort(master_array):
    master_array = sorted(master_array, key=lambda x:(x[3]-x[4]/x[3]), reverse=True)