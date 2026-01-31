from django.shortcuts import render, redirect
from .forms import CreateUserForm


def homeView(request):
    return render(request, 'home.html')

def registerView(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    
    context = {'form':form}
    return render(request, 'register.html', context)


def loginView(request):
    context = {}
    return render(request, 'login.html', context)