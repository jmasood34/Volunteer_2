from django.urls import path
from . import views

'''
This list defines the URL patterns for the application. The path() function takes three arguments:

    The first argument is the URL pattern.
    The second argument is the view function that should be called when the URL pattern is matched.
    The third argument is the name of the URL pattern.

The landing URL pattern matches the root URL of the application. The views.landing view function is called when this URL pattern is matched. 
The profile URL pattern matches the /profile/ URL. The views.profile view function is called when this URL pattern is matched. 
The update_profile URL pattern matches the /update_profile/ URL. The views.update_profile view function is called when this URL pattern is matched.
'''

urlpatterns = [
    path('', views.landing, name='landing'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile')


]
