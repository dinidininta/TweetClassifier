from django.http import HttpResponse
from django.shortcuts import render

from .forms import TweetForm
from .classification import Classification

def index(request):
    index = 'ismytweetoffensive/index.html'
    classification = Classification()

    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.cleaned_data['tweet']
            result = classification.test(tweet)

            return render(request, index, {'form': form, 'result': result})
    if request.method == 'GET':
        form = TweetForm()
    
    return render(request, index, {'form': form})