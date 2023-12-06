from django.shortcuts import render
from .forms import *

# Create your views here.
def home(req):
    if req.method == "POST":
        frm  = form1(req.POST,req.FILES)
        if frm.is_valid():
            print(frm.cleaned_data)
    else:
        frm = form1()

    return render(req, 'home.html',{'data':frm})