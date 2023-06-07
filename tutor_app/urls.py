"""
URL configuration for tutor_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # This path pattern matches the URL `/admin/`.
    # The `admin.site.urls` function is called when this URL pattern is matched.
    path("admin/", admin.site.urls),

    # This path pattern matches the root URL (`/`).
    # The `include()` function is used to include the URL patterns defined in the `user_login.urls` module.
    path('', include('user_login.urls')),

    # This path pattern matches the URL `/student_app/`.
    # The `include()` function is used to include the URL patterns defined in the `student_app.urls` module.
    path('student_app/', include('student_app.urls')),

    # This path pattern matches the URL `/teacher_app/`.
    # The `include()` function is used to include the URL patterns defined in the `teacher_app.urls` module.
    path('teacher_app/', include('teacher_app.urls')),

]
