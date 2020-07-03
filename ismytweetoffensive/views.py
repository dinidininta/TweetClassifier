from django.http import HttpResponse
from django.shortcuts import render

from .forms import TweetForm


def index(request):
    index = 'ismytweetoffensive/index.html'
    
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            return render(request, index, {'form': form, 'result': form.cleaned_data})
    if request.method == 'GET':
        form = TweetForm()
    
    return render(request, index, {'form': form})