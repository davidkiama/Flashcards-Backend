from django.db import models


# Create your models here.


class Flashcard(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
