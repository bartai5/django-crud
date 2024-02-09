from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages
# Create your views here.

def index(request):
    data = Student.objects.all()
    context = {"data":data}
    return render(request, 'index.html', context)

# Delete data from DB
def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    messages.error(request, "Data Delete Successfully.")
    return redirect("/")

# Update data to DB
def updateData(request, id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST['gender']
        age =request.POST['age']

        editkey = Student.objects.get(id=id)
        editkey.name = name
        editkey.email = email
        editkey.gender = gender
        editkey.age = age
        editkey.save()
        messages.warning(request, "Data Updated Successfully.")
        return redirect('/')
    d = Student.objects.get(id=id)
    context = {"d":d}
    
    return render(request, 'edit.html', context)

def about(request):
    return render(request, 'about.html')

# Insert data to DB
def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        age =request.POST.get('age')
        query=Student(name=name, email=email, age=age, gender=gender)
        query.save()
        messages.info(request, "Data Inserted Successfully.")
        return redirect('/')
    return render(request, 'index.html')