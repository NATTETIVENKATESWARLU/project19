from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from app.models import *
# Create your views here.
def django_form(request):
    form=nameform()
    d={'form':form}
    if request.method=='POST':
        form_data=nameform(request.POST)
        if form_data.is_valid():
            name=form_data.cleaned_data['name']
            age=form_data.cleaned_data['age']
            d={'name':name,'age':age}
            return render(request,'venkey.html',d)
        
    return render(request,'django_form.html',d)