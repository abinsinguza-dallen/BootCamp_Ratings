# from ast import If
from django.shortcuts import render
from . import Tables
from . import models

# Create your views here.
def RegStudents(request):
    if request.method=="POST":
        table=Tables.StudentsRegistrationTables(request.POST)
        if table.is_valid():
            table.save()
    else:
        table= Tables.StudentsRegistrationTables()
    return render(request,"rating/Register_student.html",{"form":table})

def students(request):
    students=models.Students.objects.all()
    return render(request, "rating/student.html",{"students":students})

def facilitators(request):
    facilitators= models.LearningFacilitators.objects.all()
    return render(request,"rating/facilitators.html",{"facilitators":facilitators})       

def learning(request):
    if request.method=="POST":
        table= Tables.LearningFacilitatorsTables(request.POST)
        if table.is_valid():
            table.save()
    else:
        table= Tables.LearningFacilitatorsTables()  
    return render(request,"rating/Register_facilitator.html",{"form":table})   

