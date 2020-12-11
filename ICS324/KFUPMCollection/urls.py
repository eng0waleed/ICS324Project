from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='KFUPMCollection/home.html'),
    path('courses/', views.courses, name='KFUPMCollection/courses.html'),
    path('about/', views.about, name='KFUPMCollection/about.html'),
    path('instructors/', views.instructors, name='KFUPMCollection/instructors.html'),
    path('instructors/evaluation/', views.evaluation, name='KFUPMCollection/instructors/evaluation.html'),
]