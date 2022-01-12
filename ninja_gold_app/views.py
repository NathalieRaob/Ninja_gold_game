from django.shortcuts import render, redirect 
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def reset(request):
    request.session.flush()
    return redirect('/')


def process(request):
    print(request.POST)
    if 'gold' not in request.session:
        request.session['gold'] = 0

    if "farm" in request.POST:
        gold = int(random.random() * 10 + 10)
        request.session['gold'] += gold
    if "cave" in request.POST:
        gold = int(random.random() * 5 + 5)
        request.session['gold'] += gold
    if "house" in request.POST:
        gold = int(random.random() * 3 + 2)
        request.session['gold'] += gold
    if "casino" in request.POST:
        gold = int(random.random() * 50)
        if int(random.random()*10) > 5:
            request.session['gold'] += gold
        else:
            request.session['gold'] -= gold
    return redirect('/')

    