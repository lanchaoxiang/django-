from django.shortcuts import render
from students.models import Students
from django.http import HttpResponseRedirect
from django.urls import reverse
from .form import StudentsForm


# Create your views here.
def index(request):
    students = Students.objects.all()
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form =StudentsForm()

    context = {
        'students':students,
        'form':form
               }
    return render(request, 'index.html', context=context)
