from .models import Teacher
from .teacher_form import TeacherForm
from django.shortcuts import render, redirect
from django.apps import apps
from .quote import daily_quote


user_data = apps.get_model('user_login', 'User')
Student = apps.get_model('student_app', 'Student')

def teacher_landing(request):
    user = request.user
    if user.is_authenticated:
        teacher, created = Teacher.objects.get_or_create(user=user, defaults={
            'phone_number': '',
            'address': '',
            'grade': '',
            'subjects': '',
            'availability_days': '',
            'availability_start': '08:00',
            'availability_end': '09:00',
            'preferred_tutoring_format': '',
            'bio': ''
        })
        first_name = user.first_name
        last_name = user.last_name
        username = user.username
        quote, author = daily_quote()

        grade = teacher.grade


        # Retrieve available students
        available_students = Student.objects.filter(user__is_student=True)



        context = {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'quote': quote,
            'author': author,
            'available_students': available_students,
        }

        return render(request, 'teacher_landing.html', context)
    else:
        return redirect('user_login:login_view')


def teacher_profile(request):
    user = request.user

    # Check if a Teacher instance exists for the user
    try:
        teacher = Teacher.objects.get(user=user)
    except Teacher.DoesNotExist:
        # If no Student instance exists, create a new one
        teacher = Teacher(user=user)

        # Set default values for other fields if needed

        teacher.phone_number = ""
        teacher.address = ""
        teacher.grade = ""
        teacher.subjects = ""
        teacher.availability_days = ""
        teacher.availability_start = "08:00"
        teacher.availability_end = "09:00"
        teacher.preferred_tutoring_format = ""
        teacher.bio = ""

        # Save the new Student instance
        teacher.save()

        # Access the first and last name from the related User object
    first_name = user.first_name
    last_name = user.last_name
    email = user.email
    username = user.username

    context = {
        'teacher': teacher,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'username': username

    }
    return render(request, 'teacher_profile.html', context)


def teacher_update_profile(request):
    user = request.user
    teacher = Teacher.objects.get(user=user)

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_profile')
    else:
        form = TeacherForm(instance=teacher)

    context = {
        'form': form
    }
    return render(request, 'teacher_update_profile.html', context)