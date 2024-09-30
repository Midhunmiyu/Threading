from django.shortcuts import render
from .models import *
from faker import Faker
fake = Faker()
from .thread import CreateStudentsThread

def home(request):
    count =100
    CreateStudentsThread(count).start()

    # for i in range(count):
    #     print(i)
    #     Students.objects.create(student_name=fake.name(),student_email=fake.email(),address=fake.address(),age=fake.random_int(min=10,max=50))
    return render(request, 'index.html')
