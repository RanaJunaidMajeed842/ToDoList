from django.shortcuts import render
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.


#Class
class newformtask(forms.Form):
        task = forms.CharField(label="New Task",
                                widget=forms.TextInput(attrs={'placeholder': 'Write Task here'}))  
#First index page
def index(request):
    if "tasks" not in request.session:
         request.session["tasks"] = []
    return render(request, "tasks/index.html",
                  {
                      "tasks":request.session["tasks"] })
#Add task page
def add(request):
    if request.method == "POST":
        forms = newformtask(request.POST)
        if forms.is_valid():
            task = forms.cleaned_data["task"]
            task = task.upper()
            request.session["tasks"] += [task]
        else:
             return render(request, "tasks/add.html",{"form":forms})
        
        
    return render(request, "tasks/add.html",{"form":newformtask()})
