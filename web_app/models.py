from django.db import models

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
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    healthRecord = models.ForeignKey(HealthRecord, on_delete=models.DO_NOTHING)

class Student(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    healthRecord = models.OneToOneField(HealthRecord, on_delete=models.CASCADE, primary_key=True,)
  
    def addRecord(self, question):
        added = RecordedQuestion(question = question, healthRecord = self.healthRecord)
        added.save()

    def __str__(self):
        return self.email