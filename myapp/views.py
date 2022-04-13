from django.shortcuts import render


from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .serializers import FlashcardSerializer
from .models import Flashcard

# Create your views here.


def index(request):
    return render(request, 'index.html')


class FlashcardViewSet(viewsets.ModelViewSet):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
