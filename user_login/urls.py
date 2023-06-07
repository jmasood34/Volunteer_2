from django.urls import path, include
from . import views

'''
This list defines the URL patterns for the application. The path() function takes three arguments:

    The first argument is the URL pattern.
    The second argument is the view function that should be called when the URL pattern is matched.
    The third argument is the name of the URL pattern.

The index URL pattern matches the root URL of the application. 
The views.index view function is called when this URL pattern is matched. 
The login URL pattern matches the /login/ URL. The views.login_view view function is called when this URL pattern is matched. 
The register URL pattern matches the /register/ URL. The views.register view function is called when this URL pattern is matched.
'''
urlpatterns = [


    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),

]
