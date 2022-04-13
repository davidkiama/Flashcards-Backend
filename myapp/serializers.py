from .models import Flashcard
from rest_framework import serializers


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ('id', 'question', 'answer', 'created_at', 'updated_at')
