from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test

# Create your views here.


def register(request):
    if request.user:
        return redirect(to='learning_log:index')

    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user=user)
            return redirect(to='learning_log:index')

    return render(request, 'registration/register.html', {'form': form})
