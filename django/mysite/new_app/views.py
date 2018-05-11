import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import SignUpForm


def current_time(request):
    now = datetime.datetime.now()
    day = now.strftime("%B %d, %Y")
    time = now.strftime("%I:%M %p")
    return HttpResponse("It is now " + time + " on " + day + ".")


class CurrentTimeTwo(View):

    def get(self, request):
        now = datetime.datetime.now()
        day = now.strftime("%B %d, %Y")
        time = now.strftime("%I:%M %p")
        return HttpResponse("It is now " + time + " on " + day + ".")


def sign_up(request):
    form = SignUpForm(request.POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        return HttpResponse("Success!")
    context = {'form': form}
    return render(request, 'signup.html', context)
