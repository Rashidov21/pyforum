from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import Category, Tag, Topic, Comment


class HomePageView(ListView):
    model = Topic
    paginate_by = 10
    context_object_name = "topics"
    template_name = "index.html"

    def get_queryset(self):
        topics = Topic.objects.all().select_related("category", "author")
        return topics


class AddNewTopicView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ["title", "category", "tag", "body"]
    success_url = "/accounts/profile/"

    def form_valid(self, form):
        print(dir(form.instance))
        form.instance.author = self.request.user
        return super().form_valid(form)


class TopicDetailView(DetailView):
    queryset = Topic.objects.select_related("category", "author")
    # queryset = Topic.objects.prefetch_related("tag")
    model = Topic

    # def get_queryset(self):
    #     topic = Topic.objects.get(slug=self.kwargs["slug"])
    #     return topic


class CategoryListView(ListView):
    model = Topic

    def get_queryset(self):
        # original qs
        qs = super().get_queryset()
        # filter by a variable captured from url, for example
        return qs.filter(category__slug=self.kwargs['slug'])


class TagListView(ListView):
    model = Topic

    def get_queryset(self):
        # original qs
        qs = super().get_queryset()
        # filter by a variable captured from url, for example
        return qs.filter(tag__slug=self.kwargs['slug'])
