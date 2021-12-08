from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from web_app.models import Student, Question, RecordedQuestion, HealthRecord

administrator_pk = 0

def log_in(request):
    # check whether student's email exist

    # if not, ask to create
        # return render(request, 'signup_page.html')


    # if exist, check password
    # if password not right

    # return render(request, 'log_in.html')
    
    # if email exist and password correct
    # update student pk
    student_pk = 1
    return redirect("main_page", student_pk)

def addNewStudent(name, email, nuid, password):
    healthRecord = HealthRecord(email = email)
    student = Student(name = name, email = email, nuid = nuid, password = password, healthRecord=healthRecord)
    healthRecord.save()
    student.save()

def sign_up(request):
    # call addNewStudent to create new student
    return redirect("log_in")

def edit_account(request, student_pk):
    student = Student.objects.get(pk = student_pk)
    context = {
        'student_pk': student_pk,
        'student': student,
    }
    return render(request, 'edit_account.html', context)

def update_account(request, student_pk):
    student = Student.objects.get(pk = student_pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        nuid = request.POST.get('nuid')
        password = request.POST.get('password')
        if name != None and len(name) > 0:
            student.name = name
        if email != None and len(email) > 0:
            student.email = email
        if nuid != None and len(nuid) > 0:
            student.nuid = nuid
        if password != None and len(password) > 0:
            student.password = password
        student.save()
    
    return redirect('edit_account', student_pk)

def main_page(request, student_pk):
    student = Student.objects.get(pk = student_pk)
    context = {
        'student_pk': student_pk,
        'name': student.name, 
        'invalid': 0,
    }
    return render(request, 'main_page.html', context)

def student_record(request, student_pk):
    student = Student.objects.get(pk = student_pk)
    
    if student_pk == administrator_pk:
        records = RecordedQuestion.objects.all()
    else:
        records = RecordedQuestion.objects.filter(student_pk = student_pk)
    
    records = reversed(records)
    context = {
        'student_pk': student_pk,
        'records': records,
        'student': student,
    }
    return render(request, 'student_record_page.html', context)


def invalid_input(request, student_pk):
    student = Student.objects.get(pk = student_pk)
    context = {
        'student_pk': student_pk,
        'name': student.name, 
        'invalid': 1,
    }
    return render(request, 'main_page.html', context)

def add_record(request, student_pk):
    student = Student.objects.get(pk = student_pk)
    if request.method == 'POST':
        symptom = request.POST.get('symptom')
        closeContact = request.POST.get('closeContact')
        result = request.POST.get('result')
        if symptom == None or closeContact == None or result == None:
            return redirect("invalid_input", student_pk)
        
        if symptom == 'True':
            symptom = True
        else:
            symptom = False
        if closeContact == 'True':
            closeContact = True
        else:
            closeContact = False
        if result == 'True':
            result = True
        else:
            result = False
        

        question = Question.objects.filter(hasSymptoms = symptom, hasCloseContact = closeContact, testResult = result)
        if len(question) > 0:
            student.addRecord(question[0])
    return redirect('student_record', student_pk)


def remove_record(request, student_pk):
    if request.method == 'POST':
        rq_pk = request.POST.get('rq_pk')
        if rq_pk != None:
            record = RecordedQuestion.objects.get(pk = rq_pk)
            if record != None:
                record.delete()
    return redirect('student_record', student_pk)