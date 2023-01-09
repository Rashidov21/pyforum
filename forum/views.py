from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import Category, Tag, Topic, Comment


class HomePageView(ListView):
    model = Topic
    paginate_by = 10
    context_object_name = "topics"
    template_name = "index.html"


class AddNewTopicView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ["title", "category", "tag", "body"]
    success_url = "/accounts/profile/"

    def form_valid(self, form):
        print(dir(form.instance))
        form.instance.author = self.request.user
        return super().form_valid(form)
