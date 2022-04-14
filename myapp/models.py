from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name


class Flashcard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    front = models.CharField(max_length=256)
    back = models.CharField(max_length=256)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save_flashcard(self):
        self.save()

    @classmethod
    def delete_flashcard(cls, id):
        '''
        Method to delete a Flashcard object
        '''
        cls.objects.filter(id=id).delete()

    @classmethod
    def get_flashcard_by_id(cls, id):
        '''
        Method to get a Flashcard by its id
        '''
        return cls.objects.filter(id=id)[0]

    @classmethod
    def get_all_flashcards(cls, id):
        '''
        Method to get all Flashcards
        '''

        return cls.objects.all()

    def __str__(self):
        return self.title
