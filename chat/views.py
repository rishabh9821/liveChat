from django.shortcuts import render
from chat import forms
from chat import forms
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    return render(request, 'chat/frontpage.html')

def signup(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('chat:home'))
    else:
        form = forms.SignUpForm()

    return render(request, 'chat/signUp.html', {'form': form})


