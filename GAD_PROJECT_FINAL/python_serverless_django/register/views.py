from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
import os


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            prefix = "C:\\Users\\stars\\Desktop\\GAD_PROJECT\\PythonServerlessApplication\\" + str(user.id)
            os.mkdir(prefix)
            os.mkdir(prefix + "\\Inputs")
            os.mkdir(prefix + "\\Scripts")
            os.mkdir(prefix + "\\DockerFiles")

        return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})
