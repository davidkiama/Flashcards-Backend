from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length = 128)

    def save_subject(self):
        self.save()

    @classmethod
    def delete_subject(cls, id):
        '''
        Method to delete a Subject object
        '''
        cls.objects.filter(id = id).delete()

    @classmethod
    def get_subject_by_id(cls, id):
        '''
        Method to get a Subject by its id
        '''
        return cls.objects.filter(id = id)[0]

    @classmethod
    def get_all_subjects(cls, id):
        '''
        Method to get all Subjects
        '''

        return cls.objects.all()

    def __str__(self):
        return self.name

class Flashcard(models.Model):
    title = models.CharField(max_length = 256)
    front = models.CharField(max_length = 256)
    back = models.CharField(max_length = 256)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def save_flashcard(self):
        self.save()

    @classmethod
    def delete_flashcard(cls, id):
        '''
        Method to delete a Flashcard object
        '''
        cls.objects.filter(id = id).delete()

    @classmethod
    def get_flashcard_by_id(cls, id):
        '''
        Method to get a Flashcard by its id
        '''
        return cls.objects.filter(id = id)[0]

    @classmethod
    def get_all_flashcards(cls, id):
        '''
        Method to get all Flashcards
        '''

        return cls.objects.all()
    
    def __str__(self):
        return self.title