from django.urls import path
from .import views

app_name = 'forum'


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('add/', views.AddNewTopicView.as_view(), name='add_topic')
]
