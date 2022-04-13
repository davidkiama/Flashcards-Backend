

from django.urls import path
from .import views


urlpatterns = [
    path('', views.FlashcardViewSet.as_view({'get': 'list'}), name='index'),
    path('home/', views.index, name='index'),
]
