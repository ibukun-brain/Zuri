from resume_app import views
from django.urls import path

app_name = 'resume_app'

urlpatterns = [
    path('projects/', views.ProjectView.as_view(), name='projects'),
    path('contact', views.contact, name='contact')
]