from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from web_app.models import Student, Question, RecordedQuestion, HealthRecord

def log_in(request):
    # check whether student's email exist

    # if not, ask to create
        # return render(request, 'signup_page.html')


    # if exist, check password
    # if password not right

    # return render(request, 'log_in.html')
    
    # if email exist and password correct
    # update student pk
    student_pk = 0
    context = {
        'student_pk': student_pk
    }
    return render(request, 'main_page.html', context)

def addNewStudent(email, password):
    healthRecord = HealthRecord(email = "zhiyulong@email.com")
    student = Student(email = email, password = password, healthRecord=healthRecord)
    healthRecord.save()
    student.save()

def sign_up(request):
    # student = Student(email, password)
    return render(request, 'log_in.html')

def main_page(request, student_pk):
    
    return render(request, 'main_page.html')

def student_record(request, student_pk):
    context = {
        'student_pk': student_pk
    }
    return render(request, 'student_record_page.html', context)


def all_records(request):
    return render(request, 'all_records_page.html')


def add_record(request, student_pk, question_pk):
    student = Student.objects.get(pk=student_pk)
    question = Question.objects.get(pk=question_pk)
    student.addRecord(question)
    return redirect('student_record_page.html', student_pk)