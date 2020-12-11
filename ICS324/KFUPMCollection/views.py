from django.shortcuts import render

from .models import departments, course, instructor


def home(request):
    context = {
        'department': departments.objects.all()
    }
    return render(request, 'KFUPMCollection/home.html', context)


def courses(request):
   
    context = {
        'courses': course.objects.all(),
         'depID': request.GET.get('depID')
    }
    return render(request, 'KFUPMCollection/courses.html', context)

def instructors(request):
    context = {
        'instructors': instructor.objects.all()
    }
    return render(request, 'KFUPMCollection/instructors.html', context)

def evaluation(request):
    
    return render(request, 'KFUPMCollection/evaluation.html')


def about(request):
    return render(request, 'KFUPMCollection/about.html')


