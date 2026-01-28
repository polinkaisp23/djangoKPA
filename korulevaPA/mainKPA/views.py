from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def RegFunc(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()      # сохраняем в БД
            login(request, user)    # автологин
            return redirect('/main/')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


@login_required(login_url='/register/')
def mainFunc(request):
    return render(request, 'main.html')