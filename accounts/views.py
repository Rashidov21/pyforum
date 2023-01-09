from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.conf import settings
from .models import User
# Create your views here.
from .forms import SimpleUserCreationForm


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile.html'


class ProfileEditView(UpdateView):
    model = User
    template_name = "registration/user_form.html"
    fields = ["first_name", "last_name", "image", "bio", "address",
              "facebook_link", "instagram_link", "telegram_link"]
    success_url = reverse_lazy("accounts:profile")


def register(request):
    form = SimpleUserCreationForm()
    if request.method == "POST":
        form = SimpleUserCreationForm(request.POST)
        if form.is_valid():
            u = form.save()
            try:
                group = Group.objects.get(name="default_user")
                group.user_set.add(u)
            except Exception as er:
                # raise
                print(er)
            print("OK")
            authenticate(u)
            message = "Successfully !"
            messages.add_message(request, messages.SUCCESS, message)
            return redirect("/")
        else:
            message = "Error !"
            messages.add_message(request, messages.ERROR, message)
            return render(request, "registration/register.html", {"form": form})

    return render(request, "registration/register.html", {"form": form})
