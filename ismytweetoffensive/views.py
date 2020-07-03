from django.http import HttpResponse
from django.shortcuts import render

from .forms import TweetForm

def index(request):
    if request.method == 'GET':
        form = TweetForm()
    
    return render(request, 'ismytweetoffensive/index.html', {'form': form})