from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'answer' not in request.session:
        request.session['answer'] = get_random_string(length=14)
        # answer = request.session['answer']
    if 'attempts' not in request.session:
        request.session['attempts'] = 1
        # attempts = request.session['attempts']
    elif 'attempts' in request.session:
        request.session['attempts'] += 1

    return render(request, 'index.html')

def reset_answer(request):
    del request.session['answer']
    return redirect('/')

def reset_attempts(request):
    del request.session['attempts']
    return redirect('/')

   

