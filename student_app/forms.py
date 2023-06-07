# forms.py

from django import forms
from .models import Student

'''
The StudentForm class is a form for creating and editing students. It inherits from the forms.ModelForm class, which provides a base class for creating forms that are bound to Django models.

The StudentForm class has the following fields:

    phone_number: The student's phone number.
    address: The student's address.
    grade: The student's grade level.
    subjects: The subjects the student is interested in tutoring.
    availability_days: The days of the week the student is available for tutoring.
    availability_start: The start time of the student's availability.
    availability_end: The end time of the student's availability.
    preferred_tutoring_format: The student's preferred tutoring format.
    goals_objectives: The student's goals and objectives for tutoring.

The StudentForm class also has the following methods:

    clean_subjects(): This method cleans the subjects field and returns a comma-separated list of the student's selected subjects.
    clean_availability_days(): This method cleans the availability_days field and returns a comma-separated list of the student's selected availability days.

'''
class StudentForm(forms.ModelForm):
    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'address'})
    )


    subjects = forms.MultipleChoiceField(
        choices=[
            ('English', 'English'),
            ('Math', 'Math'),
            ('Science', 'Science')
        ],
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )

    availability_days = forms.MultipleChoiceField(
        choices=[
            ('Monday', 'Monday'),
            ('Tuesday', 'Tuesday'),
            ('Wednesday', 'Wednesday'),
            ('Thursday', 'Thursday'),
            ('Friday', 'Friday'),
            ('Saturday', 'Saturday'),
            ('Sunday', 'Sunday')
        ],
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )

    def clean_subjects(self):
        return ','.join(self.cleaned_data['subjects'])

    def clean_availability_days(self):
        return ','.join(self.cleaned_data['availability_days'])

    class Meta:
        model = Student
        fields = ['phone_number', 'address', 'grade', 'subjects', 'availability_days',
                  'availability_start', 'availability_end', 'preferred_tutoring_format', 'goals_objectives']
