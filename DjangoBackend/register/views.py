from django.http import request
from django.shortcuts import redirect, render

from register.models import userEmailPassword, userRegestration

# Create your views here.

def register(request):
    if request.method == 'POST':
        print("post")
        emailID = request.POST["emailID"]
        p1 = request.POST["password"]
        if userEmailPassword.objects.filter(emailID=emailID).exists():
            print("This email Id has already joined")
            return redirect('/')
        else:
            user = userEmailPassword.objects.create(emailID=emailID, password = p1)
            user.save();
            print("User ", emailID, "created successfully")
            return render(request, 'loggedin.html')
    else:
        print("get1")
        return render(request, 'join.html')

def reg(request):
    return render(request, 'loggedin.html')