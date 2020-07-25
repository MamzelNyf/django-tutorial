import datetime 

from django.db import models
from django.utils import timezone

# Create your models here.

#name od the table
class Question(models.Model):
    #name of the fields
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    def __str__(self):
        # add __str__() methods to your models to create objects’ representation
        # add a method to be return the object question
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(
        Question, 
        # django adds automatically an id to represent the FK
        on_delete = models.CASCADE
        #delete the choices if the question if deleted, CASCADE function
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) 
    def __str__(self):
            return self.choice_text
