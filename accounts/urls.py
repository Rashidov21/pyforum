from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .import views

app_name = 'accounts'


urlpatterns = [
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path("profile/", views.ProfileView.as_view(), name='profile'),
    path("profile/edit/<pk>/",
         views.ProfileEditView.as_view(),
         name='profile_edit'),
    path("user/<str:username>", views.user_detail, name='user_profile'),

    path("register/", views.register, name='register')
]
