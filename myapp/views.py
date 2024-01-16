from django.http import HttpResponse
from django.shortcuts import render

import datetime


def home(request):

    isActive = True

    if request.method == 'POST':
        # check = request.POST['check']
        check = request.POST.get("check")
        print(check)
        if check is None:
            isActive = False
        else:
            isActive = True

    date = datetime.datetime.now()
    # isActive = True
    name = "Bhushan"
    list_of_programs = [
        "WAP to check even or odd",
        "WAP to check prime number",
        "WAP to print all prime numbers from 1 to 100",
        "WAP to print pascals traingle"
    ]

    student = {
        'student_name': "Rahul",
        'student_college': "XYZ",
        'student_city': "Lucknow"
    }

    data = {
        'date': date,
        'isActive': isActive,
        'name': name,
        'list_of_programs': list_of_programs,
        'student_data': student
    }
    # return HttpResponse("<h1>Hello This is Index Page </h1>"+str(date))
    return render(request, "home.html", data)


def about(request):
    # return HttpResponse("<h1> This is about page</h1>")
    return render(request, "about.html", {})


def services(request):
    # return HttpResponse("<h1> This is services page</h1>")
    return render(request, "services.html", {})
