from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import Category, Tag, Topic, Comment


class HomePageView(TemplateView):
    template_name = "index.html"


class AddNewTopicView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ["title", "category", "tag", "body"]
    success_url = "/accounts/profile/"

    def form_valid(self, form):
        print(dir(form.instance))
        form.instance.author = self.request.user
        return super().form_valid(form)
