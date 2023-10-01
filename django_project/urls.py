"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from appdamariaisabel import views


urlpatterns = [
  
  path('', views.home, name="home"),
  
  path('hobbies/', views.create_hobbie),
  path('hobbies/update/<int:id>/', views.update_hobbie),
  path('hobbies/delete/<int:id>/', views.delete_hobbie),
  
  path('learn/', views.create_learn),
  path('learn/update/<int:id>/', views.update_learn),
  path('learn/delete/<int:id>/', views.delete_learn),

  path('admin/', admin.site.urls),
]

