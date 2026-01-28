from django.shortcuts import render , redirect
from django.http  import HttpResponse
from .forms import PropertiesForm
from .models import Properties

def home(request):
    PropertiesObj = Properties.objects.all()
    return render(request, 'index.html', {'PropertiesObj': PropertiesObj})

def about(request):
    return render(request, 'about.html')

def addProperties(request):
    formObj = PropertiesForm(request.POST , request.FILES)
    if request.method == "POST":
            if formObj.is_valid():
                 formObj.save()
                 return redirect('mainpage')
    return render(request , 'addProperties.html', {'form': formObj})
