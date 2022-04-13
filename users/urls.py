from django.urls import path
from .views import RegisterView, loginView

urlpatterns =[
    path('register', RegisterView.as_view()),
    path('login', loginView.as_view())
]