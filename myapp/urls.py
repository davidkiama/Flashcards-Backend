from django.urls import path

from .views import RegisterView, loginView, UserView, logoutView, FlashcardViewSet, index


urlpatterns = [
    path('flashcards/',
         FlashcardViewSet.as_view({'get': 'list'}), name='flashcards'),

    path('home/', index, name='index'),

    path('register/', RegisterView.as_view()),
    path('login/', loginView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', logoutView.as_view()),
]
