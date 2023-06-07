from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_landing, name='teacher_landing'),
    path('teacher_profile/', views.teacher_profile, name='teacher_profile'),
    path('teacher_update_profile/', views.teacher_update_profile, name='teacher_update_profile')


]