from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Course
import datetime
from django.contrib import messages



# Create your views here.

def home(request):
    data = dict(
        courses = Course.objects.all(),
    )
    return render(request, 'home.html', context=data)


# this function handles course info from HTML form, adds it to database and displays in on html page.
def add_course(request):
    if request.method == 'POST':

        #****** VALIDATION PART *************
        errors = Course.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('home')
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the blog to be updated, make the changes, and save
        params = dict()
        
        params['name'] = request.POST.get('name')
        params['description'] = request.POST.get('description')
        params['date_added'] = datetime.datetime.now()
 
        Course.objects.create(**params)

    return redirect(reverse('home'))
        #************************************
    """params = dict()
        
        params['name'] = request.POST.get('name')
        params['description'] = request.POST.get('description')
        params['date_added'] = datetime.datetime.now()

        Course.objects.create(**params)

    return redirect(reverse('home'))"""


# This function takes the user to a specific courese page when they press the remove button.
def course_info(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course': course
    }
    return render(request, 'destroy.html', context)


# This function handles the DELETE process
def delete_course(request, id):
    #if request.method == 'POST':
        Course.objects.filter(id=id).delete()
        return redirect('home')
