from django.db import models
from django import forms
# Create your models here.

class Questionnaire(models.Model): #values start from BM id=120 and HR5 id=30
    topic = models.CharField(max_length=100)
    def __str__(self):
        return self.topic

class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire,on_delete=models.CASCADE)
    q_text = models.CharField(max_length=500)
    option_a = models.CharField(max_length=500)
    option_b = models.CharField(max_length=500)
    option_c = models.CharField(max_length=500)
    option_d = models.CharField(max_length=500)
    correct = models.CharField(max_length=5,default='E')
    def __str__(self):
        return self.q_text

# class UserAnswer(models.Model):
#     ques = models.ForeignKey(Question,on_delete=models.CASCADE, default=1)
#     answer = models.CharField(max_length=5,default='E')




