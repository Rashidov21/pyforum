from django.urls import path
from .import views

app_name = 'forum'


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('add/', views.AddNewTopicView.as_view(), name='add_topic'),
    path('detail/<slug>', views.TopicDetailView.as_view(), name='detail'),
    path("category/<slug>", views.CategoryListView.as_view(), name='category_list'),
    path("tag/<slug>", views.TagListView.as_view(), name='tag_list'),

]
