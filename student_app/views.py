
from .models import Student
from .forms import StudentForm
from django.shortcuts import render, redirect
from django.apps import apps
from .quote import daily_quote
from .reference_material import get_files_by_grade_subject



user_data = apps.get_model('user_login', 'User')
Teacher = apps.get_model('teacher_app', 'Teacher')

def landing(request):
    #get the current user
    user = request.user

    #check if user is authenticated
    if user.is_authenticated:
        # Get the student instance for the user. Create a blank instance if no student instance is present
        student, created = Student.objects.get_or_create(user=user, defaults={
            'phone_number': '',
            'address': '',
            'grade': '',
            'subjects': '',
            'availability_days': '',
            'availability_start': '08:00',
            'availability_end': '09:00',
            'preferred_tutoring_format': '',
            'goals_objectives': ''
        })
        # Get the first and last name of the user and the username
        first_name = user.first_name
        last_name = user.last_name
        username = user.username

        #get the daily quote
        quote, author = daily_quote()

        #define grade and subjects from the student instance
        grade = student.grade
        subjects = student.subjects


        # Retrieve available tutors based on student's grade
        available_tutors = Teacher.objects.filter(grade__contains=grade, user__is_tutor=True)


        # Retrieve relevant reference material based on students grade and subject
        files_by_subject = get_files_by_grade_subject(grade, subjects)

        context = {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'quote': quote,
            'author': author,
            'files_by_subject': files_by_subject,
            'grade': grade,
            'subjects': subjects,
            'available_tutors': available_tutors,

        }

        return render(request, 'landing.html', context)
    else:
        # The user is not authenticated, so redirect to the login page.
        return redirect('user_login:login_view')


def profile(request):
    # Get the current user.
    user = request.user

    # Check if a Student instance exists for the user
    try:
        student = Student.objects.get(user=user)
    except Student.DoesNotExist:
        # If no Student instance exists, create a new one
        student = Student(user=user)

        # Set default values for other fields if needed

        student.phone_number = ""
        student.address = ""
        student.grade = ""
        student.subjects = ""
        student.availability_days = ""
        student.availability_start = "08:00"
        student.availability_end = "09:00"
        student.preferred_tutoring_format = ""
        student.goals_objectives = ""

        # Save the new Student instance
        student.save()

        # Access the first and last name from the related User object
    first_name = user.first_name
    last_name = user.last_name
    email = user.email
    username = user.username

    context = {
        'student': student,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'username': username

    }
    return render(request, 'profile.html', context)


def update_profile(request):
    # Get the current user.
    user = request.user

    # Get the student instance for the user.
    student = Student.objects.get(user=user)

    # If the request method is POST, update the student instance with the data from the request.
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('profile')
    # Otherwise, render the profile page with an empty form.
    else:
        form = StudentForm(instance=student)

    context = {
        'form': form
    }
    return render(request, 'update_profile.html', context)