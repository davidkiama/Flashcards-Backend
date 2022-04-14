from django.urls import path

from .views import RegisterView, loginView, UserView, logoutView, FlashcardViewSet, index

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('flashcards/',
         FlashcardViewSet.as_view({'get': 'list'}), name='flashcards'),

    path('', index, name='index'),

    path('register/', RegisterView.as_view()),
    path('login/', loginView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', logoutView.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
