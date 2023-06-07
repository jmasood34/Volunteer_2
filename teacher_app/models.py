from django.db import models
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField

User = get_user_model()


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    grade_choices = [
        ('5th Grade', '5th Grade'),
        ('6th Grade', '6th Grade'),
        ('7th Grade', '7th Grade'),
        ('8th Grade', '8th Grade'),
        ('9th Grade', '9th Grade'),
        ('10th Grade', '10th Grade'),
    ]
    grade = MultiSelectField(choices=grade_choices, max_length=255)
    subject_choices = [
        ('English', 'English'),
        ('Math', 'Math'),
        ('Science', 'Science'),
    ]
    subjects = MultiSelectField(choices=subject_choices, max_length=255)
    day_choices = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    availability_days = MultiSelectField(choices=day_choices, max_length=255)
    availability_start = models.TimeField()
    availability_end = models.TimeField()
    preferred_tutoring_format_choices = [
        ('Online', 'Online'),
        ('In Person', 'In Person'),
    ]
    preferred_tutoring_format = MultiSelectField(choices=preferred_tutoring_format_choices, max_length=255)
    bio = models.TextField()

