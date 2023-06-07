from django.db import models
from django.contrib.auth.models import AbstractUser



# Create SQL table for user data


class User(AbstractUser):
    is_student = models.BooleanField('Is student', default=False)
    is_tutor = models.BooleanField('Is tutor', default=False)

