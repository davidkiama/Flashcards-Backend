from django.urls import path
from .views import RegisterView, loginView, UserView, logoutView

urlpatterns =[
    path('register', RegisterView.as_view()),
    path('login', loginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', logoutView.as_view()),
]