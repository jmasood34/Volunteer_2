# forms.py

from django import forms
from .models import Teacher


class TeacherForm(forms.ModelForm):
    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'address'})
    )

    grade = forms.MultipleChoiceField(
        choices=[
            ('5th Grade', '5th Grade'),
            ('6th Grade', '6th Grade'),
            ('7th Grade', '7th Grade'),
            ('8th Grade', '8th Grade'),
            ('9th Grade', '9th Grade'),
            ('10th Grade', '10th Grade'),
        ],
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
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

    preferred_tutoring_format = forms.MultipleChoiceField(
        choices=[
            ('Online', 'Online'),
            ('In Person', 'In Person'),
        ],
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )

    def clean_grade(self):
        return ','.join(self.cleaned_data['grade'])

    def clean_subjects(self):
        return ','.join(self.cleaned_data['subjects'])

    def clean_availability_days(self):
        return ','.join(self.cleaned_data['availability_days'])

    def clean_preferred_tutoring_format(self):
        return ','.join(self.cleaned_data['preferred_tutoring_format'])

    class Meta:
        model = Teacher
        fields = ['phone_number', 'address', 'grade', 'subjects', 'availability_days',
                  'availability_start', 'availability_end', 'preferred_tutoring_format', 'bio']
