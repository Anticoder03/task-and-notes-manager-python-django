"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from core.views import index, add_note, view_notes, add_task, view_tasks


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('add-note/', add_note, name='add_note'),
    path('notes/', view_notes, name='view_notes'),
    path('add-task/', add_task, name='add_task'),
    path('tasks/', view_tasks, name='view_tasks'),
]
