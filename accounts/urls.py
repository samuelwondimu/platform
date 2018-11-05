from django.urls import path, include
from knox.views import LogoutView, LogoutAllView
from accounts.views import RegistrationView, LoginView, UserView

urlpatterns = [
    path("register/", RegistrationView.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("logoutall/", LogoutAllView.as_view()),
    path("users/", UserView.as_view({'get': 'list'}))
]
