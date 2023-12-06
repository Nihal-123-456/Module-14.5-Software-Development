from django.shortcuts import render
from .import models
# Create your views here.
def home(request):
    md = models.model1.objects.all()
    return render(request,'home.html',{'data':md})