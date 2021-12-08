from django.db import models
import datetime

# Create your models here.
class Question(models.Model):
    hasSymptoms = models.BooleanField()
    hasCloseContact = models.BooleanField()
    testResult = models.BooleanField()

class HealthRecord(models.Model):
    email = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question, through='RecordedQuestion')  
    
    def __str__(self):
        return "Health Record for Student: " + self.email

class RecordedQuestion(models.Model):
    student_pk = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    healthRecord = models.ForeignKey(HealthRecord, on_delete=models.DO_NOTHING)
    time = models.DateTimeField(null=True)

class Student(models.Model):
    name = models.CharField(max_length=100, null=True, default='no name recorded')
    email = models.CharField(max_length=100)
    nuid = models.CharField(max_length=20, null=True, default='no nuid recorded')
    password = models.CharField(max_length=100)
    healthRecord = models.OneToOneField(HealthRecord, on_delete=models.CASCADE, primary_key=True,)
  
    def addRecord(self, question):
        time = datetime.datetime.now()
        added = RecordedQuestion(student_pk = self.pk, question = question, healthRecord = self.healthRecord, time = time)
        added.save()

    def __str__(self):
        return self.email