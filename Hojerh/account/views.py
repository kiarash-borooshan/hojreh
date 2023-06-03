from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import RegisterForm, RegisterProfileForm


def register_user(request: HttpRequest):

    if request.method == "POST":

        """ register user """
        form = RegisterForm(request.POST)
        profile_form = RegisterProfileForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user: User = form.save(commit=False)
            user.set_password(cd['password'])
            user.save()

            return HttpResponse("Created account")

    else:
        form = RegisterForm()
        profile_form = RegisterProfileForm()

    return render(request,
                  'account/register.html',
                  {'form': form,
                   'profile_form': profile_form})
