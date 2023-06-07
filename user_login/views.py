from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
# Create your views here.


def index(request):

    # This function renders the `index.html` template.
    return render(request, 'index.html')


def register(request):

    # This function registers a new user.
    # The `msg` variable is used to store a message that is displayed to the user.
    msg = None

    # If the request method is POST, then the form data is processed.
    if request.method == 'POST':

        # The `form` variable is created by passing the request data to the `SignUpForm` class.
        form = SignUpForm(request.POST)

        # If the form is valid, then a new user is created and the `msg` variable is set to a message indicating that the user was created successfully.
        if form.is_valid():

            # The `user` variable is created by calling the `save()` method on the `form` object.
            user = form.save()

            # The `msg` variable is set to a message indicating that the user was created successfully.
            msg = 'user created'

            # The user is redirected to the login page.
            return redirect('login_view')

        # If the form is not valid, then the `msg` variable is set to a message indicating that the form was not valid.
        else:
            msg = 'form is not valid'

    # If the request method is not POST, then an empty `form` object is created.
    else:
        form = SignUpForm()

    # The `msg` variable is passed to the `render()` function along with the `form` object.
    return render(request, 'register.html', {'form': form, 'msg': msg})


def login_view(request):

    # This function logs a user in.
    # The `msg` variable is used to store a message that is displayed to the user.
    msg = None

    # The `form` variable is created by passing the request data to the `LoginForm` class.
    form = LoginForm(request.POST or None)

    # If the request method is POST, then the form data is processed.
    if request.method == 'POST':

        # If the form is valid, then the user is authenticated and logged in.
        if form.is_valid():

            # The `username` and `password` variables are retrieved from the `form` object.
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # The `user` variable is created by calling the `authenticate()` function.
            user = authenticate(username=username, password=password)

            # If the `user` variable is not None, then the user is logged in.
            if user is not None:

                # The user is logged in by calling the `login()` function.
                login(request, user)

                # If the user is a student, then the user is redirected to the student landing page.
                if user.is_student:
                    return redirect(reverse('landing'))

                # If the user is a tutor, then the user is redirected to the teacher landing page.
                elif user.is_tutor:
                    return redirect(reverse('teacher_landing'))

            # If the `user` variable is None, then the `msg` variable is set to a message indicating that the user credentials were invalid.
            else:
                msg = 'invalid credentials'

        # If the form is not valid, then the `msg` variable is set to a message indicating that the form was not valid.
        else:
            msg = 'error validating form'

    # The `msg` variable is passed to the `render()` function along with the `form` object.
    return render(request, 'login.html', {'form': form, 'msg': msg})
