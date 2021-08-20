from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, CreateView
from .models import Contact

# Create your views here.
class IndexView(TemplateView):
    template_name = 'resume_app/index.html'

class ProjectView(TemplateView):
    template_name = 'resume_app/projects.html'

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']


        contact = Contact(name=name, email=email, phone=phone, message=message)

        contact.save()

        messages.success(request, 'Your request has been submitted, I will get back to you soon')

        return redirect('index')