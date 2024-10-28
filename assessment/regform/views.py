from django.shortcuts import render,redirect

from django.urls import reverse
from .forms import SignupForm
# Create your views here.
def index(request):
    form= SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.fname= user.fname.Upper()
            user.lname= user.lname.Upper()
            user.save()
            return redirect()
    return render(request,'regform/signup.html',{"form":form})
