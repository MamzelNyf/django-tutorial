from django.db import models

# Create your models here.

#name od the table
class Question(models.Model):
    #name of the fields
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

class Choice(models.Model):
    question = models.ForeignKey(
        Question, 
        # django adds automatically an id to represent the FK
        on_delete = models.CASCADE
        #delete the choices if the question if deleted, CASCADE function
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)